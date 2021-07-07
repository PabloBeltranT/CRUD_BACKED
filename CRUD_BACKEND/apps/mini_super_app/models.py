from django.db import models

# Create your models here.
class miniSuperModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    paternal_surname = models.CharField(max_length=50, null=False)
    maternal_surname = models.CharField(max_length=50, null=False)
    age = models.DecimalField(max_digits=2, decimal_places=0)
    email = models.EmailField(max_length=254, null=False, unique=True)
    phone = models.DecimalField(max_digits=10, decimal_places=0, unique=True, null=False)

    def __str__(self):
        return self.name

