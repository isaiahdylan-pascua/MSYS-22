from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    
    def getName(self):
        return self.name

    def __str__(self):
        return self.name + " - " + self.city + ", " + self.country + " created at: " + str(self.created_at)
    
class WaterBottle(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0, null=False)
    size = models.CharField(max_length = 50)
    mouth_size = models.CharField(max_length = 100)
    color = models.CharField(max_length=50)
    supplied_by =  models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quant = models.IntegerField(default=0, null=False)
    objects = models.Manager()

    def __str__(self):
        return self.sku + ":" + self.brand + ",", self.mouth_size + "," + self.color \
        + "supplied by" + self.supplied_by(Supplier.getName()) + "," + self.cost + ":" + self.current_quant
    
