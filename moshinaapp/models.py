from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class moshina(models.Model):
    moshina_name=models.CharField(max_length=60)
    price=models.IntegerField()
