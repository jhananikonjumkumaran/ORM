# Ex02 Django ORM Web Application
## Date: 06.10.2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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


admin.py
from django.contrib import admin
from .models import vehicle_info,vehicle_info_Admin
admin.site.register(vehicle_info,vehicle_info_Admin)


```


## OUTPUT
![alt text](image.png)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
