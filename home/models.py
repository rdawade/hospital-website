from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    desc = models.TextField()
    date = models.DateField()

