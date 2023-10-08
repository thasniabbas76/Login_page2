from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber= models.CharField(max_length=15)
    description = models.TextField()
    def __str__(self):
        return self.name