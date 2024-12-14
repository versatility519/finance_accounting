from django.db import models

from apps.inventory.models import OrderUnit
from apps.organization.models import Tax, Department

from apps.account.models import LedgerAccount

from apps.users.models import CustomUser

# Create your models here.
class PurchaseDocument(models.Model):
    doc_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    docdoc_filefile = models.FileField(upload_to='documents/purchase_docs')
    purchase_order = models.ForeignKey('PurchaseOrder', related_name='documents', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class PurchaseOrderItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    manufacturer_code =  models.CharField(max_length=100)
    measure_unit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE)
    supplier_code = models.CharField(max_length=100)
    
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=100, choices=[
        ('created', 'Created'), 
        ('approved', 'Approved'), 
        ('partially_received', 'Partially received'),
        ('completed', 'Completed')
    ])
    
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    reception_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    received = models.BooleanField(default=False)
    purchaseOrder = models.ForeignKey('PurchaseOrder', related_name='items', on_delete=models.CASCADE)    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name
    
    def save(self, *args, **kwargs):
        if self.tax_group:
            self.tax_amount = self.quantity * self.price * self.tax_group.tax_rate
        else:
            self.tax_amount = 0
        self.net_amount = self.quantity * self.price
        super().save(*args, **kwargs)
    
class PurchaseOrder(models.Model):
    po_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField()
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    order_unit = models.ForeignKey('inventory.OrderUnit', on_delete=models.CASCADE)

    status = models.CharField(max_length=100, choices=[
        ('created', 'Created'),
        ('approved', 'Approved'),
        ('partially_received', 'Partially_received'),
        ('completed', 'Completed'),
        ('sent', 'Sent'),
        ('canncelled', 'Canncelled')
    ])
     
    # approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.po_name