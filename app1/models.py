from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    stud_name = models.CharField(max_length=100)
    stud_email = models.CharField(max_length=100)
    stud_contact = models.BigIntegerField()
    stud_address = models.TextField()


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    teacher_email = models.CharField(max_length=100)
    teacher_contact = models.BigIntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)    