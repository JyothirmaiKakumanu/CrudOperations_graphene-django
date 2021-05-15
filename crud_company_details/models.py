from django.db import models

# Create your models here.
class Company_Details(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    owner_info = models.CharField(max_length=100)
    employee_size = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    