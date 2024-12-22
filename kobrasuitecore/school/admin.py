# school/admin.py

from django.contrib import admin
from .models import Course, Assignment, Submission, StudyGroup, StudyNote

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')
    filter_horizontal = ('students',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date', 'created_at')
    search_fields = ('title', 'course__title')
    list_filter = ('due_date', 'created_at')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submitted_at', 'grade')
    search_fields = ('assignment__title', 'student__username')
    list_filter = ('submitted_at',)

@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ('name', 'course__title')
    filter_horizontal = ('members',)

@admin.register(StudyNote)
class StudyNoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'course', 'assignment', 'created_at')
    search_fields = ('author__username', 'course__title', 'assignment__title')
    filter_horizontal = ('shared_with',)
