from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# username, calories, and date.

class FoodFitnessModel(models.Model):
    username= models.CharField(max_length=200)
    calories= models.DecimalField(max_digits=5,decimal_places=2)
    date= models.DateField(default=timezone.now())
    identificationKey= models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.username