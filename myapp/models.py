from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class food(models.Model):
    name=models.CharField(max_length=100)
    carbs=models.FloatField()
    protein=models.FloatField()
    fats=models.FloatField()
    calories=models.IntegerField()

    def __str__(self):
        return self.name

class consume(models.Model):
    food_consumed=models.ForeignKey(food,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)