from django.db import models

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'
        verbose_name = "prestamo"
        verbose_name_plural = "prestamos"

    def __str__(self): 
        return self.loan_type

