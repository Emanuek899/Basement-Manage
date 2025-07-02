from django.db import connection, IntegrityError
from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(unique=True, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'categories'


class ProductCategories(models.Model):
    pk = models.CompositePrimaryKey('product_id', 'category_id')
    product = models.ForeignKey('Products', models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_categories'