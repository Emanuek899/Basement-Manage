from django.db import connection, IntegrityError
from django.db import models

# Create your models here.
class Providers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number1 = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'providers'


class ProductProviders(models.Model):
    pk = models.CompositePrimaryKey('product_id', 'provider_id')
    product = models.ForeignKey('products.Products', models.DO_NOTHING)
    provider = models.ForeignKey('providers.Providers', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'product_providers'