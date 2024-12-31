from rest_framework import viewsets
from .models import Course, Assignment, Submission

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    # serializer_class = CourseSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    # serializer_class = AssignmentSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    # serializer_class = SubmissionSerializer