from django.db import models

# Create your models here.
class catogery(models.Model):
    p_pid=models.IntegerField()
    p_product=models.CharField(max_length=30)
    p_price=models.IntegerField()
    class Meta:
        db_table="catogery"
class product(models.Model):
    l_id=models.IntegerField()
    l_product=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    l_price=models.IntegerField()
    class Meta:
        db_table="product"