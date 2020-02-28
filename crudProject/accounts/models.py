from django.contrib.auth.models import User
from django.db import models

class RegistrationModel(models.Model):

    contact_no = models.IntegerField(unique=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
