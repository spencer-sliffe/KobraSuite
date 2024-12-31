from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from .models import Role
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    RoleSerializer
)

User = get_user_model()


@method_decorator(csrf_exempt, name='dispatch')
class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'register':
            return RegisterSerializer
        elif self.action == 'login':
            return LoginSerializer
        elif self.action == 'logout':
            return LoginSerializer
        elif self.action == 'whoami':
            return UserSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ['register', 'login', 'logout']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @action(methods=['post'], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
            except IntegrityError:
                return Response(
                    {"errors": "Username or email already taken."},
                    status=status.HTTP_409_CONFLICT
                )
            user_data = UserSerializer(user).data
            return Response(
                {
                    "success": True,
                    "message": "User registered successfully.",
                    "user": user_data
                },
                status=status.HTTP_201_CREATED
            )
        # Validation failed
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Additional check: Is user active?
                if not user.is_active:
                    return Response(
                        {"errors": "User account is disabled."},
                        status=status.HTTP_403_FORBIDDEN
                    )
                login(request, user)
                user_data = UserSerializer(user).data
                return Response(
                    {
                        "success": True,
                        "message": "Logged in successfully.",
                        "user": user_data
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "errors": "Invalid credentials."},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        # Serializer not valid
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(methods=['post'], detail=False)
    def logout(self, request):
        logout(request)
        return Response({"success": True, "message": "Logged out successfully."}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def whoami(self, request):
        if request.user.is_authenticated:
            user_data = UserSerializer(request.user).data
            return Response({"user": user_data}, status=status.HTTP_200_OK)
        return Response({"detail": "Not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer