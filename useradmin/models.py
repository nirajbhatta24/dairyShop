from django.db import models



# Create your models here.

class Useradmin(models.Model):

    id=models.AutoField(auto_created=True,primary_key=True)

    username=models.CharField(max_length=100)

    email = models.CharField(max_length=100,unique=True)

    password=models.CharField(max_length=8)



    class Meta:

        db_table="useradmin"