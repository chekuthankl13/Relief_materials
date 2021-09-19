from django.db import models

# Create your models here.


class Donor(models.Model):
    doid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'donor'
