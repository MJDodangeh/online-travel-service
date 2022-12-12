from django.db import models


class user(models.Model):
    username=models.CharField(max_length=256)
    password=models.CharField(max_length=256)
    first_name=models.CharField(max_length=128)
    last_name= models.CharField(max_length=128)
    phone_number=models.CharField(max_length=20)
    national_code=models.CharField(max_length=20)
    birthday_date=models.DateTimeField()


