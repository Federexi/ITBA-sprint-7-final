# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from Clientes.models import Cliente

class MarcaTarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_brand = models.TextField()

    class Meta:
        db_table = 'marca_tarjeta'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    card_number = models.TextField(unique=True)
    cvv = models.TextField(db_column='CVV')  # Field name made lowercase.
    valid_from = models.DateField()
    xpiration_date = models.DateField()
    card_type = models.TextField()
    cardbrand_id = models.ForeignKey(MarcaTarjeta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tarjeta'