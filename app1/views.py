from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .helpers import send_forgot_password_mail
import uuid

from app1.models import Profile, Student

# Create your views here.
def home_fun(request):
    return render(request, 'home.html')

def login_fun(request):
    if request.method == 'POST':
        user_name = request.POST['txtName']
        user_password = request.POST['txtPassword']
        u1 = authenticate(username=user_name, password=user_password)
        if u1 is not None:
            if u1.is_superuser:
                request.session['Uname'] = user_name
                login(request, u1)
                return redirect('teacher_home')
            else:
                request.session['Uname'] = user_name
                login(request, u1)
                return redirect('student_home')
        else:
            return render(request, 'login.html', {'Msg': 'Username and password is not matching with each other'})
    else:           
        return render(request, 'login.html')
    
def teacher_login_fun(request):
    if request.method == 'POST':
        user_name = request.POST['txtName']
        user_password = request.POST['txtPassword']
        t1 = authenticate(username=user_name, password=user_password)
        if t1 is not None:
            if t1.is_superuser:
                request.session['Tname'] = user_name
                login(request, t1)
                return redirect('teacher_home')
            else:
                return render(request, 'studenthome.html')
        else:
            return render(request, 'teacherlogin.html', {'Msg': 'Username and Password is not matching'})
    else:
        return render(request, 'teacherlogin.html')    



def teacher_register_fun(request):
    if request.method == 'POST':
        user_name = request.POST['txtName']
        user_contact = int(request.POST['txtContact'])
        user_email = request.POST['txtEmail']
        user_password = request.POST['txtPassword']
        if User.objects.filter(username=user_name).exists():
            return render(request, 'teacherregister.html', {'Msg': 'Username already exist'})
        elif User.objects.filter(email=user_email).exists():
            return render(request, 'teacherregister.html', {'Msg': 'Email already exist'})
        else: 
            t1 = User.objects.create_superuser(username=user_name, password=user_password, email=user_email)
            t1.save()
            return redirect('teacher_login')
    else:        
        return render(request, 'teacherregister.html')

def register_fun(request):
    if request.method == 'POST':
        user_name = request.POST['txtName']
        user_contact = int(request.POST['txtContact'])
        user_email = request.POST['txtEmail']
        user_address = request.POST['txtAddress']
        user_password = request.POST['txtPassword']
        if User.objects.filter(username=user_name).exists():
            return render(request, 'register.html', {'Msg': 'Username already exist'})
        elif User.objects.filter(email=user_email).exists():
            return render(request, 'register.html', {'Msg': 'Email already exist'})
        else:
            u1 = User.objects.create_user(username=user_name, password=user_password, email=user_email)
            u1.save()
            return redirect('login')
    else:    
        return render(request, 'register.html')    
    

@login_required
@never_cache
def teacher_home_fun(request):
    return render(request, 'teacherhome.html', {'Data': request.session['Tname']})


@login_required
@never_cache
def student_home_fun(request):
    return render(request, 'studenthome.html', {'Data': request.session['Uname']})


@login_required
@never_cache
def add_student_fun(request):
    if request.method == 'POST':
        s1 = Student()
        s1.stud_name = request.POST['txtName']
        s1.stud_contact = int(request.POST['txtContact'])
        s1.stud_email = request.POST['txtEmail']
        s1.stud_address = request.POST['txtAddress']
        s1.save()
        return render(request, 'addstudent.html', {'Msg': 'Data Added Successfully'})
    else:
        return render(request, 'addstudent.html')
    
@login_required
@never_cache
def student_details_fun(request):
    stud_data = Student.objects.all()
    return render(request, 'studentdetails.html', {'StudentData': stud_data})

@login_required
@never_cache
def display_student_fun(request):
    stud_data = Student.objects.all()
    return render(request, 'displaystudent.html', {'StudentData': stud_data})


def logout_fun(request):
    logout(request)
    return redirect('home')


def change_password_fun(request, token):
    context = {}
    profile = Profile.objects.get(forgot_password_token=token)
    print(profile)
    return render(request, 'changepassword.html')


def forgot_password_fun(request):
    if request.method == 'POST':
        user_name = request.POST['txtUsername']
        if not User.objects.filter(username=user_name).exists():
            return render(request, 'forgotpassword.html', {'Msg': 'No user found by this username'})
        user_object = User.objects.get(username=user_name)
        token = str(uuid.uuid4())
        send_forgot_password_mail(user_object, token)
        return render(request, 'forgotpassword.html', {'Msg': 'An Email is sent for password change'})
    return render(request, 'forgotpassword.html')