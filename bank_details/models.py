from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Banks(models.Model):
    """
    Model for Banks
    fields:
    name : Bank Name
    id : Primary key for Bank names
    """
    name = models.CharField(max_length=49)
    id = models.BigIntegerField(primary_key=True)


class Branches(models.Model):
    """
    Model for Branches details of all Banks
    fields:
    ifsc: IFSC code which is a unique code for all branches of all banks
    bank_id : Foreign key for Banks model
    branch: Branch name
    address : Address of the branch
    """
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id = models.ForeignKey(Banks,on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)




