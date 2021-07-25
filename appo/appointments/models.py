# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.deletion import CASCADE
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name_error'] = "Name must be 2 or more characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        if len(postData['password']) < 8 or len(postData['confirm_password']) < 8:
            errors['pass_length'] = "Password must be 8 or more characters"
        if postData['password'] != postData['confirm_password']:
            errors['pass_match'] = "Passwords must match"
        if User.objects.filter(email=postData['email']):
            errors['exists'] = "Email ya existe"
        return errors
    
    def login(self, postData):
        errors = {}
        try:
            val_email = User.objects.get(email=postData['email'])
            if postData['email'] == val_email.email:
                user = User.objects.get(email=postData['email'])
                if not bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
                    errors['wrong_password'] = "Contraseña invalida!!"
                return errors
        except:
            errors['not_user'] = "E-mail no registrado! Registrese antes de hacer login!!"
        return errors
class AppointmentManager(models.Manager):

    def validator(self, postData):
        errors = {}
        if len(postData['task']) < 2:
            errors['task_length'] = "Task must be at least 2 characters"



class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Appointment(models.Model):
    task = models.CharField(max_length=255)
    date = models.DateField(blank=False, null=True, default=False)
    time = models.TimeField()
    CATEGORY_CHOICES = (
            ("Pending", "Pending"),
            ( "Missed", "Missed"),
            ( "Done", "Done"),
            )
    status = models.CharField(max_length=255, choices = CATEGORY_CHOICES)
    user_appointments = models.ForeignKey(User, related_name="appointments",  on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AppointmentManager()