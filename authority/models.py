from django.db import models

# Create your models here.


class Authority(models.Model):
    address = models.TextField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'authority'
