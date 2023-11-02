from django.db import models
from wisdomacademy.models import Course
from wisdomacademy.options import STATUS_CHOICES
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100,  null= True, blank=True)
    # email = models.EmailField(unique=True ,  null= True, blank=True)
    gender = models.CharField(max_length=10,  null= True, blank=True)
    premium_student = models.BooleanField(default=False)
    date_of_birth = models.DateField( blank=True, null=True)
    phone_number = models.CharField(max_length=20,  null= True, blank=True)
    address = models.CharField(max_length=20,  null= True, blank=True)
    profile_picture = models.ImageField(upload_to='student_profile_pics/', blank=True, null=True)
    courses = models.ManyToManyField('wisdomacademy.Course', through='Enrollment')
    category = models.CharField(max_length=20, choices=[('teacher', 'teacher'), ('student', 'student')], default='student')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('wisdomacademy.Course', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enrolled')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.user} enrolled in {self.course.class_title}"

    # So that a student dont enroll in a partical course twice
    class Meta:
        unique_together = ('student', 'course')




class Review(models.Model):
    course = models.ForeignKey('wisdomacademy.Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)