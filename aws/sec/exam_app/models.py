from django.db import models
from login_registration_app.models import *

# Modelos creados
class TripManager(models.Manager):
    def trip_validator(self, postData):
        todays_date = datetime.now().date()
        date_format = "%Y-%m-%d"

   

        errors = {}

        

        if len(postData['destination']) < 5:
            errors['destination'] = "Group must be at least 5 characters"
        
        if len(postData['plan']) < 10:
            errors['plan'] = "Descripcion must be at least 10 characters"

        

        return errors

        

class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    #start_date = models.DateField()
    #end_date = models.DateField()
    plan = models.TextField()
    created_by = models.ForeignKey(User, related_name = "trips", on_delete = models.CASCADE)
    joined_by = models.ManyToManyField(User, related_name = "joined_trips")
    objects = TripManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)