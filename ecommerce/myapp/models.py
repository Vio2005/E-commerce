from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=255)
    def __str__(self):
        return self.category_name
    

class Items(models.Model):
    item_name=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    photo=models.ImageField(upload_to='photo')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.item_name
    
class Cartitem(models.Model):
    items=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    qty=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    

