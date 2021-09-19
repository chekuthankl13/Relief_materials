from django.db import models

# Create your models here.



class Awareness(models.Model):
    date = models.DateField()
    awareness = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'awareness'
