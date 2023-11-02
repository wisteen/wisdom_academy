from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User 
from .models import UserProfile
from student.models import Student



class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class StudentInline(admin.StackedInline):
	model = Student
	can_delete = False



class AccountUserAdmin(UserAdmin):
	def add_view(self, *arg, **kwargs):
		self.inlines = []
		return super(AccountUserAdmin, self).add_view(*arg, **kwargs)


		
	def change_view(self, *arg, **kwargs):
		self.inlines = [UserProfileInline, StudentInline]
		return super(AccountUserAdmin, self).change_view(*arg, **kwargs)



admin.site.unregister(User)
admin.site.register(User, AccountUserAdmin)
