from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField, IntegerField, TextField
import re,bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def form_validator(self, postData):
        errors = {}
        try:
            val_email = User.objects.get(email=postData['email'])
            #if int(postData['usr_id']) != User.objects.get(email=postData['email']).id:
            if postData['email'] == val_email.email:
                errors['email'] = "Correo electronico ya se encuentra registrado!!"
        except:
            if postData['update_type'] == 'pwrd':
                if len(postData['password']) <8 or len(postData['confirm_password']) <8:
                    errors['passwords'] = "Contraseña debe tener al menos 8 caracteres!!"
                if postData['password'] != postData['confirm_password']:
                    errors['cconfirm_password'] = "Las contraseñas no coinciden!!"
            else:
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
                if not EMAIL_REGEX.match(postData['email']):   
                    errors['email'] = "Direccion de e-mail invalida!!"
            
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
    email = EmailField(max_length=100)
    password = CharField(max_length=100)
    user_level = IntegerField()
    description = TextField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = UserManager()
