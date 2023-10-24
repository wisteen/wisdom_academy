from django.urls import path
from . import views

app_name = "teacher"
urlpatterns = [
    path('teacher', views.register_teacher, name='register_teacher'),
    path('info', views.info_page, name='info_page'),
    path('update', views.update_profile, name='update_profile'),
    path('login', views.login_teacher, name='login_teacher'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]