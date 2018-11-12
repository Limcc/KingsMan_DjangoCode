from django.db import models

# Create your models here.

class product(models.Model):
    photo=models.ImageField()
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    code=models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.code) +" "+ self.name +" "+ self.category


class productPhoto(models.Model):
    photo = models.ImageField()
    code = models.ForeignKey("product", on_delete=models.CASCADE)