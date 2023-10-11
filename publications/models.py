from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.db import models
from accounts.models import Account, Profesion

class Publication(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    mini_content = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='publications/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Relación ForeignKey con Account
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
