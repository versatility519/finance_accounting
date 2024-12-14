from django.db import models
from apps.users.models import CustomUser
# Create your models here.
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name   
      
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name
   
