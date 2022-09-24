from django.db import models
from django.conf import settings

# Create your models here.


# class AppUser(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=50)
#     date_created = models.DateTimeField(auto_now_add=True)
#     username = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     is_author = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)


class Newsletter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/')
    # image = models.ImageField(upload_to='images/')
    active = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
