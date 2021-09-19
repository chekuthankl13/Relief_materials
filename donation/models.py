from django.db import models
from donor.models import Donor
from camp.models import Camp

#from donation_request.models import DonationRequest
# Create your models here.


class Donation(models.Model):
    did = models.AutoField(primary_key=True)
    time = models.TimeField()
    detail = models.CharField(max_length=30)
    date = models.DateField()
    amount = models.IntegerField()
    status = models.CharField(max_length=30)
    #cid = models.IntegerField()

    #doid = models.IntegerField()
    #request = models.CharField(max_length=30)
    #request = models.ForeignKey(DonationRequest, on_delete=models.CASCADE)
    do = models.ForeignKey(Donor, to_field='doid', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'donation'
