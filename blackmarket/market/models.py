from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)