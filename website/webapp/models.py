from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
      return self.title

class Images(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField() 
    Images=models.ImageField(upload_to='images')
    addes_date =models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
