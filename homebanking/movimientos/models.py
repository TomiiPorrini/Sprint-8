from django.db import models

# Create your models here.

class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True)
    num_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'
        verbose_name = "moviento"
        verbose_name_plural = "movimientos"
