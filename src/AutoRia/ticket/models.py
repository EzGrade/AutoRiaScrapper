from django.db import models


# Create your models here.
class Ticket(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price_usd = models.IntegerField()
    odometer = models.IntegerField()
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    images_count = models.IntegerField()
    car_number = models.CharField(max_length=255)
    car_vin = models.CharField(max_length=255)
    datatime_found = models.DateTimeField(auto_now_add=True)
