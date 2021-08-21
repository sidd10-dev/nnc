from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE)
    address = models.TextField()
    phone_no = models.CharField(max_length=10)
    def __str__(self):
        return str(self.user.username)
