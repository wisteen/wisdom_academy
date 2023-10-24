from django.db import models
from wisdomacademy.models import Course
from wisdomacademy.options import STATUS_CHOICES
from ckeditor.fields import RichTextField
# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    premium_student = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='student_profile_pics/', blank=True, null=True)
    courses = models.ManyToManyField('wisdomacademy.Course', through='Enrollment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('wisdomacademy.Course', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enrolled')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.class_title}"

    # So that a student dont enroll in a partical course twice
    class Meta:
        unique_together = ('student', 'course')