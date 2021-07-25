from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeField, EmailField
from datetime import datetime, date, timedelta
import re,bcrypt
from django.db.models.fields.related import ForeignKey

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def form_validator(self, postData):
        errors = {}
        current_date = date.today()
        try:
            val_email = User.objects.get(email=postData['email'])
            if postData['email'] == val_email.email:
                errors['email'] = "Correo electronico ya se encuentra registrado!!"
        except:
            if len(postData['fname']) < 2:
                errors['fname'] = "El nombre del usuario debe ser mayor a 2 caracteres!!"
            else:
                if postData['fname'].isalpha() == False:
                    errors['fname'] = "El nombre del usuario debe tener solo letras!!"
            if len(postData['lname']) < 2:
                errors['description'] = "El apellido del usuario debe ser mayor a 2 caracteres!!"
            else:
                if postData['fname'].isalpha() == False:
                    errors['lname'] = "El apellido del usuario debe tener solo letras!!"
            if postData['dob'] >= current_date.strftime("%Y-%m-%d"):
                errors['dob'] = "La fecha de nacimiento no puede estar hoy o en el futuro!!"
            birt_date = datetime.strptime(postData['dob'], '%Y-%m-%d').date()
            if (current_date - birt_date) < timedelta(days=4745):
                errors['too_old'] = "Usuario no puede tener menos de 13 años!!"
            if not EMAIL_REGEX.match(postData['email']):   
                errors['email'] = "Direccion de e-mail invalida!!"
            if postData['password'] != postData['confirm_password']:
                    errors['cconfirm_password'] = "Las contraseñas no coinciden!!"
            else:
                if len(postData['password']) <8 or len(postData['confirm_password']) <8:
                    errors['passwords'] = "Contraseña debe tener al menos 8 caracteres!!"
        return errors
    def login_validator(self, postData):
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

class User(models.Model):
    fname = CharField(max_length=50)
    lname = CharField(max_length=50)
    dob = DateField()
    email = EmailField(max_length=100)
    password = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = UserManager()




