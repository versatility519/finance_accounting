from django.db import models
# from apps.supplier.models import Supplier, SupplierContact
from apps.inventory.models import OrderUnit
from apps.account.models import LedgerAccount    
from apps.organization.models import Tax

from apps.purchaseOrder.models import PurchaseOrder

class BillDoc(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    doc_file = models.FileField(upload_to='documents/bills') 
    bill = models.ForeignKey('Bill', related_name='billDocs', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
 
class Terms(models.Model):
    name = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class BillItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    measure_unit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE)
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    net_amount = models.DecimalField(max_digits=10, decimal_places=3)
    
    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    
    bill = models.ForeignKey('Bill', related_name='items', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
 
    def save(self, *args, **kwargs):
        print("Saving InvoiceItem...")
        if self.tax_group:
            self.tax_amount = self.quantity * self.price * self.tax_group.tax_rate
        else:
            self.tax_amount = 0
        self.net_amount = self.quantity * self.price
        super().save(*args, **kwargs)

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    bill_num = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE)
    required_date = models.DateField()
    
    status = models.CharField(max_length=20, choices=[
        ('need approval', 'Need approval'),
        ('approve', 'Approve'),
        ('waiting Payment', 'Waiting Payment'),
        ('paid', 'Paid'),
        ('completed', 'Completed'),
        ('close', 'Close')
    ])
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)

    terms = models.ForeignKey('Terms', on_delete=models.CASCADE)

    total_net_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    
    contact = models.ForeignKey('supplier.SupplierContact', on_delete=models.CASCADE, null=True, blank=True)    
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.bill_num)
    
    def save(self, *args, **kwargs):
        self.name = f"Bill-{self.bill_num}" 
        super().save(*args, **kwargs) 
