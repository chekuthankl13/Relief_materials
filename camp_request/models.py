from django.db import models

# Create your models here.


class CampRequest(models.Model):
    date = models.DateField()
    request = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'camp_request'
