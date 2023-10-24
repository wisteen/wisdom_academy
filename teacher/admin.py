from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User 
from .models import UserProfile



class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class AccountUserAdmin(UserAdmin):
	def add_view(self, *arg, **kwargs):
		self.inlines = []
		return super(AccountUserAdmin, self).add_view(*arg, **kwargs)
		
	def change_view(self, *arg, **kwargs):
		self.inlines = [UserProfileInline]
		return super(AccountUserAdmin, self).change_view(*arg, **kwargs)
	# inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, AccountUserAdmin)
