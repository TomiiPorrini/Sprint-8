from django.db import models

# Create your models here.
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    customer_direccion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.TextField()
    card_expire = models.TextField()
    card_expire_date = models.TextField()
    card_cvv = models.IntegerField()
    card_type = models.TextField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'

class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    calle = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    employee_direccion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'