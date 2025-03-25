from django.db import models


# Create your models here.
class Connection(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class ClientCompany(models.Model):

    class TypeChoice(models.TextChoices):
        CUSTOMER = 'customer', 'CUSTOMER'
        COMPANY = 'company', 'COMPANY'

    full_name = models.CharField(max_length=255)
    image = models.ImageField()
    position = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=0)
    type = models.CharField(max_length=255, choices=TypeChoice.choices, default=TypeChoice.CUSTOMER)


    '''Service connection'''
class ServiceContact(models.Model):
    connection = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
