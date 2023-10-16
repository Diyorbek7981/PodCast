from django.db import models
from django.urls import reverse


# Create your models here.

class Contact(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    phone = models.CharField(verbose_name='Phone', max_length=40)
    subject = models.CharField(verbose_name='Subject', max_length=200)
    message = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse ('contact',)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(verbose_name='Email', max_length=200)

    def __str__(self):
        return self.email
