from django.db import models
from django.contrib.auth.models import User
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
	category = models.CharField(max_length=20, null= True, blank=True)
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

