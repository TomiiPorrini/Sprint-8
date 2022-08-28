from django.db import models

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
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self): 
        return self.customer_name + " " + self.customer_surname