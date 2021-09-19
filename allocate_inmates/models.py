from django.db import models

#--------------------------------
#from inmates.models import Inmates

# Create your models here.


class AllocateInmates(models.Model):
    date = models.DateField()
    donation = models.IntegerField()
    iid = models.CharField(max_length=50)
    cid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'allocate_inmates'



# class Donation(models.Model):
#     detail = models.CharField(max_length=30)
    #------------------------------------------------------------------------
   # iid =  models.ForeignKey(Inmates,to_field='iid',on_delete=models.CASCADE)
#-------------------------------------------------------------------------------
