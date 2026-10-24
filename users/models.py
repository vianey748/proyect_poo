from django.db import models

# Create your models here
class Users(models.Model):

     class sexType(models.IntegerField):
          MALE = (1,"male")
          FEMALE = (2, "female")
          OTHER = (3, "other")

     username = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     birth_date = models.DateField(null=False)
     password = models.CharField(max_length=10, blank=False, null=False)
     sex = models.IntegerField(choicecs=sexType.choices,
                               default=sexType.OTHER)
     phone = models.IntegerField() 