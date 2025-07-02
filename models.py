# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Token(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=True)  # This field type is a guess.
    key = models.CharField()

    class Meta:
        managed = False
        db_table = 'token'


class Users(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=True)  # This field type is a guess.
    username = models.CharField(unique=True)
    email = models.CharField(unique=True)
    pass_field = models.CharField(db_column='pass')  # Field renamed because it was a Python reserved word.
    date_sign = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'users'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'categories'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ProductCategories(models.Model):
    pk = models.CompositePrimaryKey('product_id', 'category_id')
    product = models.ForeignKey('Products', models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_categories'


class ProductProviders(models.Model):
    pk = models.CompositePrimaryKey('product_id', 'provider_id')
    product = models.ForeignKey('Products', models.DO_NOTHING)
    provider = models.ForeignKey('Providers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_providers'


class Products(models.Model):
    name = models.CharField(unique=True, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Providers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number1 = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'providers'


class Token(models.Model):
    key = models.CharField(max_length=64)
    users = models.ForeignKey('Users', models.DO_NOTHING, db_column='users')

    class Meta:
        managed = False
        db_table = 'token'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=100)
    pass_field = models.CharField(db_column='pass', max_length=20)  # Field renamed because it was a Python reserved word.
    position = models.TextField()
    date_sign = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
