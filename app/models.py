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

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Category(BaseModel):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=1)
    sub_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
        )

    def __str__(self):
        return self.name


class Service(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    spend_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Info(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length=255)
    order = models.IntegerField(default=1)
