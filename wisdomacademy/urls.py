from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CourseDetailView
# from .views import home

app_name = "wisdom"
urlpatterns = [
    path('', views.home , name='home'),
    path('join', views.join , name='login'),
    path('register', views.register , name='register'),
    path('about', views.about , name='about'),
    path('contact', views.contact , name='contact'),
    path('course', views.course , name='course'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:course_id>/add_review/', views.add_review, name='add_review'),

]