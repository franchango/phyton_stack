from django.db import models
import bcrypt
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validator(self, postData):
        todays_date = datetime.now().date()
        date_format = "%Y-%m-%d"
        
        input_date = datetime.strptime(postData['birthday'], date_format).date()

        math_delta = todays_date-input_date
        math_string = str(math_delta)
        math_split = math_string.split()
        math_days = math_split[0]
        math_years = int(math_days)/365

        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "El nombre debe tener al menos 2 letras"

        if not postData['first_name'].isalpha():
            errors['first_name_alpha'] = "El nombre debe contener solo letras"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "El apellido debe tener al menos 2 letras"

        if not postData['last_name'].isalpha():
            errors['last_name_alpha'] = "El apellido debe contener solo letras"

        if not postData['birthday']:
            errors['birthday'] = "Por favor, introduzca su fecha de nacimiento"
    
        if math_years < 16:
            errors['birthday'] = "Debe tener 16 años o más para utilizar este sitio. Busca a un adulto.."

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Por favor, introduce una dirección de correo electrónico válida."

        email_unique_check = User.objects.filter(email=postData['email'])

        if email_unique_check:
            errors['email'] = "Ingrese un correo electrónico único."


        if len(postData['password']) < 8:
            errors['password'] = "La contraseña debe tener al menos 8 caracteres."

        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Las contraseñas no coinciden"


        return errors

    def register(self, postData):
        safe_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()

        return User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], birthday=postData['birthday'], email=postData['email'], password = safe_password)

    def authenticate(self, email, password):
        users = User.objects.filter(email = email)
        if users:
            user = users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return True
        
        return False


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    birthday = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
# modelos 