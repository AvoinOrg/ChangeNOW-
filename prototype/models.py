from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=30)
    id = models.PositiveIntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False, null=False, unique= True)

    def __str__(self):
        return self.name
    
class Offer(models.Model):
    company = models.CharField(max_length=30)
    id = models.PositiveIntegerField(primary_key=True)
    price = models.DecimalField(max_digits=50, decimal_places=2, default="")
    greenness = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class Bid(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=50, decimal_places=2, default="")
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name