from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120, blank=False, null=True)

    email = models.EmailField(blank=False, null=True)

    subject = models.CharField(max_length=80, blank=False, null=True)

    message = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.subject
