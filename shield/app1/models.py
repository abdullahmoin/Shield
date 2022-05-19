from django.db import models


# Create your models here.

class Contacts(models.Model):
    fast_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    subject = models.TextField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject
