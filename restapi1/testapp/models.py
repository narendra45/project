from django.db import models

class ProductModel(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name
