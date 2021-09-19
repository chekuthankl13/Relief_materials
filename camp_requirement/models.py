from django.db import models

# Create your models here.


class CampRequirement(models.Model):
    crid = models.AutoField(primary_key=True)
    date = models.DateField()
    requirements = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'camp_requirement'
