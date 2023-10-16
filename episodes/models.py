from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='images/users/')
    job = models.CharField(max_length=60)

    def __str__(self):
        return self.username


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    podcast = models.ForeignKey('Podcast', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    podcast = models.ForeignKey('Podcast', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Likes'
        verbose_name = 'Like'


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Tags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Podcast(models.Model):
    # autor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='images/podcasts/')
    file = models.FileField(upload_to='files/')
    about = models.TextField()
    guests = models.ManyToManyField(User, blank=True)
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title
