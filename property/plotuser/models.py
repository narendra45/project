from django.db import models

class PlotUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_cont_no = models.IntegerField()
    user_mail = models.EmailField()
    user_address = models.CharField(max_length=200)

