from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class RoundModel(models.Model):
    is_active = models.BooleanField(default=True)


class MoveModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="moves")
    round = models.ForeignKey(RoundModel, on_delete=models.CASCADE, related_name="history")
    value = models.IntegerField(null=True)
    jackpot = models.BooleanField(default=False)
