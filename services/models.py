from django.db import models

# Create your models here.
class Category(models.Model):
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    mini_content = models.CharField(max_length=255)

    def __str__(self):
        return self.profession
    
class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.name

