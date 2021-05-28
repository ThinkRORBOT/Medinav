from django.db import models

class usrCredentials(models.Model):
    u_id = models.IntegerField(default='0')
    u_name = models.CharField(max_length = 20, default = '')
    # will be encrypted later on
    u_pwd = models.TextField(default = '')

    # this should go to a separate database later on
class mixedDrugs(models.Model):
    d_id = models.IntegerField(default='0')
    d_name = models.CharField(max_length = 100, default = '')

class ingrediantList(models.Model):
    i_id = models.IntegerField(default = '0')
    i_name = models.CharField(max_length = 100, default = '')
    location = models.IntegerField(default = '0')
    required = models.CharField(max_length = 2, default = 'F')
    concentration = models.CharField(max_length=20, default='')

# external reference to d_id and i_id
class drugIngrediant(models.Model):
    i_id = models.IntegerField(default = '0')
    d_id = models.IntegerField(default = '0')
    amount = models.FloatField(default = '0')
    units = models.CharField(max_length=50,default='g')
