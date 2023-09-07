from django.db import models
from .options import *
# from ckeditor.fields import CKEditorWidget # This is for form
from ckeditor.fields import RichTextField
class CourseCat(models.Model):
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    course_description = models.TextField()
    
    def __str__(self):
        return f"{self.category}"
# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100, choices=COURSE_NAME)
    content = RichTextField()
    course_description = models.TextField()
    course_duration = models.CharField(max_length=20)
    course_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    course_topic = models.TextField()
    course_material = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course_name} - {self.course_topic}" 
    
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    specialization = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='instructor_profile_pics/', blank=True, null=True)
    def __str__(self):
        return f"{self.name}"


class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    premium_student = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='student_profile_pics/', blank=True, null=True)
    courses = models.ManyToManyField('Course', through='Enrollment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enrolled')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
    
class Payment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Payment for {self.course.name} by {self.student.name}"