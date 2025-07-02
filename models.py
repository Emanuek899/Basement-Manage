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
