from django.urls import path
from app1 import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_fun, name='home'),
    path('login', views.login_fun, name='login'),
    path('register', views.register_fun, name='register'),
    path('student_home', views.student_home_fun, name='student_home'),
    path('teacher_home', views.teacher_home_fun, name='teacher_home'),
    path('teacher_login', views.teacher_login_fun, name='teacher_login'),
    path('teacher_register', views.teacher_register_fun, name='teacher_register'),
    path('add_student', views.add_student_fun, name='add_student'),
    path('student_details', views.student_details_fun, name='student_details'),
    path('display_student', views.display_student_fun, name='display_student'),
    path('logout', views.logout_fun, name='logout'),
    path('change_password/<token>', views.change_password_fun, name='change_password'),
    path('forgot_password', views.forgot_password_fun, name='forgot_password'),



]