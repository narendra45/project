from django.db import models
class Tags(models.Model):
    tags_name=models.CharField(max_length=30)

    def __str__(self):
        return self.tags_name

class ProductDetails(models.Model):

    product_name=models.CharField(max_length=30)
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to="media/products_images/")

    CATEGORY_CHOICES = (
        ('Mobile', 'mobile'),
        ('Tv', 'tv'),
        ('Grocery','grocery')
    )
    category = models.CharField(max_length=30,choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.product_name


