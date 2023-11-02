from django.contrib import admin
from .models import Course, Tag #, Instructor, Student,Enrollment, Payment
# Register your models here.
class CourseDisplay(admin.ModelAdmin):
    list_display = ("class_title", "instructor", "is_active" )
    search_fields = ("class_title", "instructor", "is_active")
    list_per_page = 25
    
admin.site.register(Course, CourseDisplay)
admin.site.register(Tag)
# admin.site.register(Instructor)
# admin.site.register(Student)
# admin.site.register(Enrollment)
# admin.site.register(Payment)
