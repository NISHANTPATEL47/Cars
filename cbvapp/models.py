from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    origin=models.CharField(max_length=100)
    est_year=models.IntegerField()
    company_logo = models.ImageField(upload_to="image/", blank=True, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()
    seat_capacity = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    milige = models.IntegerField()
    company = models.ForeignKey(Company, related_name='companies', on_delete=models.CASCADE)
