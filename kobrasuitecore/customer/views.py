# customer/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout

from .models import Role
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthViewSet(viewsets.GenericViewSet):
    """
    A ViewSet for user authentication: register, login, logout.
    """
    queryset = User.objects.all()

    def get_permissions(self):
        # register & login can be accessed by anyone
        if self.action in ['register', 'login']:
            self.permission_classes = [AllowAny]
        else:
            # logout or any other actions require the user to be authenticated
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @action(methods=['post'], detail=False)
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # create the user
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # session-based login
                return Response({"message": "Logged in successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def logout(self, request):
        logout(request)
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Add permission classes, filtering, etc., as desired


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    # You can create a RoleSerializer or reuse something else
    # serializer_class = RoleSerializer  (not shown in this snippet)