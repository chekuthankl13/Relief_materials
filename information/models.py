from django.db import models

# Create your models here.


class Information(models.Model):
    information = models.CharField(max_length=30)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'information'
