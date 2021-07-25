# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.deletion import CASCADE
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors= {}
        if len(postData["name"]) < 2:
            errors["name"] = "El nombre debe ser mayor a 2 caracteres"           
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Dirección de correo no válida"
        repeated_email = User.objects.filter(email = postData["email"])
        if len(repeated_email) > 0:
            errors["email"] = "La dirección de correo electrónica ya se encuentra registrada"
            
        if len(postData["password"]) < 8:
            errors["password"] = "La longitud del password debe ser de al menos 8 caracteres"
            
        if postData["password"] != postData["password_confirm"]:
            errors["password_no_coincide"] = "Las contraseñas ingresadas no coinciden."
            
        if dob.strptime(postData["dob"], '%Y-%m-%d') > datetime.now():
            errors["fecha_incorrecta"] = "La fecha seleccionada no puede ser mayor que le fecha actual."
        
        dob = datetime.strptime(postData["dob"], '%Y-%m-%d')
        edad = relativedelta(datetime.now(), dob)
        if edad.years < 18:
            errors["edad"]= "Debe ser mayor de 13 años para poder registrarse"
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