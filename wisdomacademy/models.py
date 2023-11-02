from django.db import models
from .options import *
from teacher.models import UserProfile
from django.contrib.auth.models import User
# from student.models import Student
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_image = models.ImageField(upload_to='course/', blank=True, null=True)
    class_title = models.CharField(max_length=100)
    max_number_of_student = models.CharField(max_length=100)
    content = RichTextField()
    class_description = models.TextField(max_length=300)
    full_description_and_curriculum = RichTextField()
    class_duration = models.CharField(max_length=20)
    course_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    class_status = models.CharField(max_length=100, choices=(("Pending", "Pending"),("Upcoming", "Upcoming"), ("Completed", "Completed"), ("Ongoing", "Ongoing")))
    course_material =  RichTextField()
    instructor = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    class_price = models.CharField(max_length=8)
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_reviews(self):
        return Review.objects.filter(course=self)

    def __str__(self):
        return f"{self.class_title}" 
    





# class Instructor(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()
#     specialization = models.CharField(max_length=100)
#     profile_picture = models.ImageField(upload_to='instructor_profile_pics/', blank=True, null=True)
#     def __str__(self):
#         return f"{self.name}"    
# class Payment(models.Model):
#     student = models.ForeignKey('Student', on_delete=models.CASCADE)
#     course = models.ForeignKey('Course', on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=8, decimal_places=2)
#     payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"Payment for {self.course.name} by {self.student.name}"