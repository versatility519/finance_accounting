from django.db import models
from apps.inventory.models import OrderUnit
from apps.project.models import Project
from apps.users.models import CustomUser

# Create your models here.
class Pdocument(models.Model):
    doc_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to='documents/productions')
    production = models.ForeignKey('Production', related_name='documents', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.doc_name
    
class ProductionItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    
    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)
    
    measure_unit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE, related_name='products')
    
    approved = models.BooleanField(default=False)
    approved_quantity = models.IntegerField(default=0)
    
    status = models.CharField(max_length=100)
   
    production = models.ForeignKey('Production', on_delete=models.CASCADE, related_name='items')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.approved:
            self.approved_quantity = self.quantity
        super().save(*args, **kwargs)
        
class Production(models.Model):
    p_name = models.CharField(max_length=100)
    date = models.DateField()
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='productions') 
    p_start_date = models.DateTimeField(auto_now_add=True)
    p_end_date = models.DateTimeField(auto_now_add=True)
    
    p_status = models.CharField(max_length=32, choices=[
            ('create', 'Create'), 
            ('waiting_approval', 'Waiting_approval'), 
            ('approve', 'Approve'),
            ('started', 'Started'),
            ('ended', 'Ended'),
        ]
    )
     
    # created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='productions')
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='productions')
    
    def __str__(self):
        return self.p_name