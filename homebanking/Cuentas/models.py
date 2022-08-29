from django.db import models

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    type_account_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'
        verbose_name = "cuenta"
        verbose_name_plural = "cuentas"