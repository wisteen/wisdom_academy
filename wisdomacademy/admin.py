from django.contrib import admin
from .models import Course, Instructor, Student,Enrollment, Payment
# Register your models here.
class CourseDisplay(admin.ModelAdmin):
    list_display = ("course_topic", "course_name", "course_level" , "course_duration", "is_active")
    search_fields = ("course_topic", "course_name", "course_level" , "course_duration", "is_active")
    list_per_page = 25
    
admin.site.register(Course, CourseDisplay)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Payment)
