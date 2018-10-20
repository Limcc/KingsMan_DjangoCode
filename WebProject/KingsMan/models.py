from django.db import models

# Create your models here.

class product(models.Model):
    photo=models.ImageField()
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    size=models.IntegerField()
    category=models.CharField(max_length=100)
    code=models.AutoField(primary_key=True)

    def __str__(self):
        return self.name +" "+ self.category