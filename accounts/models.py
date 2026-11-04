from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.mail import send_mail

class User(AbstractUser):

    phone = models.CharField(max_length=12,unique=True)

    ROLE_CHOICES = (
        ("student","student"),
        ("admin","admin")
    )

    role = models.CharField(max_length=100,choices=ROLE_CHOICES,default="student")

class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=20,null=True)

    github_url = models.URLField(null=True)

    linkedin_url = models.URLField(null=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")

def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,User)

def send_invitation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        send_mail(
            "Account creation confirmation",
            "You have successfully created account in CodePilot",
            "vasudevcptb@gmail.com",
            ["soorajvk135@gmail.com"],
                )

post_save.connect(send_invitation_mail,sender=User)
