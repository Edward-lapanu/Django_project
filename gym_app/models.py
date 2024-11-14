from django.db import models

# Create your models here.
class Appointment(models.Model):
    ''' Appointment table '''
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    service = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)  # Message is optional
   

    def __str__(self):
        return f"Appointment with {self.name}"

