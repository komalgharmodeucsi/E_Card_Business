from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mob_no = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = "web_member"


class Person(models.Model):
    firstname = models.CharField(max_length=30, default="")
    lastname = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=30, default="")
    mob = models.CharField(max_length=12, default="")
    password = models.CharField(max_length=12, default="")
    c_password = models.CharField(max_length=12, default="")

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = "person"


class Design(models.Model):
    image_id = models.AutoField
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="Card_App/images", default="")

    def __str__(self):
        return self.name


    class Meta:
        db_table = "product"

##############################################################################################Payment


