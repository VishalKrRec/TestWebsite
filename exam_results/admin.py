from django.contrib import admin
from .models import Test, TestResult, Student, Subject

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "roll_number",
    ]


@admin.register(Subject)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = [
        "subject",
        "date",
    ]


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "test",
        "score"
    ]
