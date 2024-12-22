from django.db import models
from django.conf import settings

class Course(models.Model):
    """
    Represents a course/class a user is enrolled in.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='courses', 
        blank=True
    )

    def __str__(self):
        return self.title


class Assignment(models.Model):
    """
    Tasks or homework linked to a course.
    """
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='assignments'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"


class Submission(models.Model):
    """
    A student's submission for an assignment.
    """
    assignment = models.ForeignKey(
        Assignment, 
        on_delete=models.CASCADE, 
        related_name='submissions'
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='submissions'
    )
    file = models.FileField(upload_to='assignment_submissions/', null=True, blank=True)
    text_answer = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Submission by {self.student.username} for {self.assignment.title}"


class StudyGroup(models.Model):
    """
    A small group for collaborative learning.
    """
    name = models.CharField(max_length=100)
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='study_groups'
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='study_groups', 
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.course.title}"


class StudyNote(models.Model):
    """
    Notes for a course or assignment; can be shared with others.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='study_notes'
    )
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='notes'
    )
    assignment = models.ForeignKey(
        Assignment, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='notes'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        blank=True, 
        related_name='received_notes'
    )

    def __str__(self):
        return f"Study Note by {self.author.username}"

