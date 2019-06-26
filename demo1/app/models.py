from django.db import models

# Create your models here.
class manage(models.Model):
    username = models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    types=models.CharField(max_length=20)
    db_table="manage"