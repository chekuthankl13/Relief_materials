from django.db import models

# Create your models here.

class Inmates(models.Model):
    iid = models.AutoField(primary_key=True)
    age = models.IntegerField()
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'inmates'
