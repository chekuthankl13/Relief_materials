from django.db import models

# Create your models here.



class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    uid = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'login'
