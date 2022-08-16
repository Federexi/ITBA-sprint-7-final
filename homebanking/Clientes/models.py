# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
# Unable to inspect table 'tipocliente'
# The error was: cannot unpack non-iterable NoneType object

class TipoCliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    cu_type = models.TextField()

    class Meta:
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField()
    branch_id = models.IntegerField()
    customer_type = models.ForeignKey(TipoCliente, models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def approve_loan(self, amount):
        if self.customer_type == 'BLACK' and amount <= 500000:
            return True

        if self.customer_type == 'GOLD' and amount <= 300000:
            return True

        if self.customer_type == 'CLASSIC' and amount <= 100000:
            return True
        return False

    class Meta:
        db_table = 'cliente'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        db_table = 'empleado'
