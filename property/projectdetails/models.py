from django.db import models

class PlotDetails(models.Model):
    plot_no = models.IntegerField(primary_key=True)
    plot_image = models.ImageField(upload_to="plot_images/")
    road_no = models.IntegerField()
    survey_no = models.IntegerField()
    cost_per_sqd = models.DecimalField(max_digits=20,decimal_places=2)
    other_exp = models.DecimalField(max_digits=10,decimal_places=2)
    boundaries = models.IntegerField()
    facing = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    Total_cost = models.DecimalField(max_digits=20,decimal_places=2)

class AppartmentDetails(models.Model):
    app_type = models.CharField(max_length=100)
    app_no = models.IntegerField(primary_key=True)
    app_image = models.ImageField(upload_to="appartment_images/")
    app_area= models.DecimalField(max_digits=20,decimal_places=2)
    app_floor_type = models.CharField(max_length=100)
    app_age = models.IntegerField()
    app_cost = models.DecimalField(max_digits=20,decimal_places=2)
    other_exp = models.DecimalField(max_digits=10,decimal_places=2)
    facing = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    total_cost = models.DecimalField(max_digits=20,decimal_places=2)






