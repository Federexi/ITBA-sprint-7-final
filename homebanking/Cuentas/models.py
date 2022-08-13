# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'tipocuenta'
# The error was: cannot unpack non-iterable NoneType object

class TipoCuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    ac_type = models.TextField()

    class Meta:
        db_table = 'tipo_cuenta'

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey(TipoCuenta, models.DO_NOTHING)
    type = models.TextField()

    class Meta:
        db_table = 'cuenta'


class Movimientos(models.Model):
    movement_id = models.AutoField(primary_key=True)
    no_account = models.IntegerField()
    amount = models.IntegerField()
    type_operation = models.TextField()
    hour = models.DateField()

    class Meta:
        db_table = 'movimientos'
