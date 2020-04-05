
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Chat(models.Model):
    sender= models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, )
    message=models.CharField(max_length=100)
    recieverid=models.IntegerField(null=True)
    reciever=models.CharField(max_length=50)



