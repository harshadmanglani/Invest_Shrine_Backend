from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    category_name = models.CharField(max_length = 60)

    class Meta:
        verbose_name_plural = "Category"
    
    def __str__(self):
        return str(self.category_name) if self.category_name else ''

    
class User(AbstractUser):
    email = models.EmailField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = "Category" , default = 1)

    #REQUIRED_FIELDS = ['category',]





