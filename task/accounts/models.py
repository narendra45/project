from django.contrib.auth.models import User
from django.db import models

class Otp(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact=models.IntegerField()
    otp = models.IntegerField(null=True)
    otp_verified=models.BooleanField(default=False)

class Credentials(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    credential_name=models.CharField(max_length=100)
    credential=models.CharField(max_length=100)