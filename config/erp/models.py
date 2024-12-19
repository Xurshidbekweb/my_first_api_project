from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Student(models.Model):
    group = models.ForeignKey(Group,on_delete=models.PROTECT)
    full_name = models.CharField(max_length=150,verbose_name="Ismi")
    age = models.PositiveIntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(6)
    ],verbose_name="Yosh")
    address = models.CharField(max_length=150,null=True,blank=True,verbose_name="Manzil")
    phone_number = models.CharField(max_length=13,verbose_name="Telefon raqam")
    email = models.EmailField()


    def __str__(self):
        return self.full_name
