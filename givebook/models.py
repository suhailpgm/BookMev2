from django.db import models
from django.conf import settings


class Bookadd(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, )
    bookname= models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    language= models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    Bookadd_img = models.ImageField(upload_to='images/')
    isbno=models.IntegerField()
    availability=models.IntegerField(default=1)
    pageno= models.IntegerField(null=True)
    reqid=models.IntegerField(null=True)
    reqname=models.CharField(max_length=50)

