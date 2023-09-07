from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import Permission, Group 
# from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=20, null= True, blank=True)
	qualifications = models.TextField(blank=True, null= True)
	short_description = models.TextField(blank=True)
	sex = models.CharField(max_length=10, blank=True, null= True)
	years_of_experience = models.PositiveIntegerField(blank=True, null= True)
	cv = models.FileField(upload_to='cv/', blank=True, null= True)
	picture = models.ImageField(upload_to='dp/', blank=True, null= True)
	application_letter = models.FileField(upload_to='applications/', blank=True, null= True)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)



# Create your models here.
# class Teacher(AbstractUser):
#     phone_number = models.CharField(max_length=20)
#     qualifications = models.TextField()
#     short_description = models.TextField(blank=True)
#     sex = models.CharField(max_length=10)
#     years_of_experience = models.PositiveIntegerField()
#     cv = models.FileField(upload_to='cv/')
#     application_letter = models.FileField(upload_to='applications/')
#     is_approved = models.BooleanField(default=False)
#     # Add related_name attributes to avoid clash with User model
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name='groups',
#         blank=True,
#         related_name='teacher_groups',  # Change this to a suitable name
#         related_query_name='teacher',
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name='user permissions',
#         blank=True,
#         related_name='teacher_user_permissions',  # Change this to a suitable name
#         related_query_name='teacher',
#     )
