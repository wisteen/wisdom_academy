from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User 
from .models import Student, Enrollment, Review
from teacher.admin import UserProfileInline
# Register your models here.

class StudentInline(admin.StackedInline):
	model = Student
	can_delete = False

class StudentUserAdmin(UserAdmin):
	def add_view(self, *arg, **kwargs):
		self.inlines = [UserProfileInline]
		return super(AccountUserAdmin, self).add_view(*arg, **kwargs)
		
	def change_view(self, *arg, **kwargs):
		self.inlines = [StudentInline]
		return super(StudentUserAdmin, self).change_view(*arg, **kwargs)

# admin.site.unregister(User)
# admin.site.register(User, StudentUserAdmin)

# admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Review)
