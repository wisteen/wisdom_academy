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
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
# Register your models here.

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = [ 'email', 'is_approved']

#     actions = ['approve_teachers']
#     add_fieldsets = UserAdmin.add_fieldsets +  (
#     	(None, {'fields':('email', 'first_name', 'last_name', 'username')})
#     	)
#     fieldset = UserAdmin.fieldsets + (
#     	(None, {'fields':('email', 'first_name', 'last_name', 'username')})
#     	)
#     def approve_teachers(self, request, queryset):
#         queryset.update(is_approved=True)
#     approve_teachers.short_description = "Approve selected teachers"