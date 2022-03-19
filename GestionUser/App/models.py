
from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField('Nom',max_length=30)
    email= models.EmailField('Email')
    def __str__(self):
        return self.first_name

class Article(models.Model):
     headline= models.CharField(max_length=30)
     pub_date= models.DateField()
     created_at= models.DateTimeField(auto_now_add=True)
     updated_at= models.DateTimeField(auto_now=True)
     est_valide= models.BooleanField(default=True)
     reporter= models.ForeignKey(
         Reporter, on_delete=models.CASCADE,
     )
     def __str__(self):
         return self.headline