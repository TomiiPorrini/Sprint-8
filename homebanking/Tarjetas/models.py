from django.db import models

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.IntegerField()
    card_expire = models.IntegerField()
    card_expire_date = models.IntegerField()
    card_cvv = models.IntegerField()
    card_type = models.TextField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'
        verbose_name = "tarjeta"
        verbose_name_plural = "tarjetas"
