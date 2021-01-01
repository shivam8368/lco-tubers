from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    subject = models.TextField()
    message = models.TextField()
    date_created = models.DateTimeField(blank=True, default=datetime.now)


    def __str__(self):
        return self.email