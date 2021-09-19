from django.db import models

# Create your models here.


class DonationRequest(models.Model):
    cid = models.IntegerField()
    date = models.DateField()
    request = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'donation_request'

class Bchain(models.Model):
    chdata = models.CharField(max_length=1000)
    hashv = models.CharField(max_length=1000)
    phash = models.CharField(max_length=1000)
    tstamp = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'bchain'

