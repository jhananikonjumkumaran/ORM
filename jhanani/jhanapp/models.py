from django.db import models
from django.contrib import admin
class vehicle_info(models.Model):
    vehicle_no_plate=models.CharField(max_length=8,primary_key=True)
    brand_name=models.CharField(max_length=10)
    vehicle_type=models.CharField(max_length=15)
    date_of_purchase=models.DateField()
    colour=models.CharField(max_length=10)
    owner_mob_no=models.IntegerField()
    owner_address=models.TextField()
class vehicle_info_Admin(admin.ModelAdmin):
    list_display=["vehicle_no_plate","brand_name","vehicle_type","date_of_purchase","colour","owner_mob_no","owner_address"]
