from django.db import models
# Create your models here.

class Address(models.Model):
    address = models.TextField()
    postal_code = models.PositiveIntegerField()

    def __str__(self):
        return self.address
