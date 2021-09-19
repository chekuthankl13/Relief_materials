from django.db import models

# Create your models here.


class Camp(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    date = models.DateField()
    place = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'camp'

