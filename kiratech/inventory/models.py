from django.db import models


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    note = models.TextField(max_length=255)
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='suppliers')
