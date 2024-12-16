from django.db import models
from apps.user.models import User
from apps.account.models import LedgerAccount
from apps.purchaseOrder.models import PurchaseOrder
from apps.inventory.models import InventoryItem

class Carrier(models.Model):
    name = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    billing_address = models.TextField(max_length=200)
    shipping_address = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE, null=True, blank=True)
    inventory_items = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name='inventory_suppliers',
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.supplier_name)

class SupplierItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    sku = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    measure_unit = models.ForeignKey('inventory.OrderUnit', on_delete=models.CASCADE)   
    growth = models.BooleanField(default=False)
    growth_fre = models.CharField(max_length=100, choices=[
        ('weekly', 'Weekly'),
        ('bi_weekly', 'Bi-Weekly'),
        ('monthly', 'Monthly'),
        ('quaters', 'Quarterly'),
        ('half_yearly', 'Half-Yearly'),
        ('yearly', 'Yearly'),
    ])
    growth_per = models.FloatField()
    supplier = models.ForeignKey(Supplier, related_name='supplier_items', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
        
class SupplierContact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    role = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, related_name='supplier_contact', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ShippingItem(models.Model):
    shipping_name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    manufacturer_code = models.CharField(max_length=50)
    item_code = models.CharField(max_length=100)
    
    shipping = models.ForeignKey('Shipping', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.shipping_name

class ShipDocs(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to='documents/shipping')
    shipping = models.ForeignKey('Shipping', related_name='shipping_docs', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.doc_name
    
class Shipping(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    sent_by = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    shipping_date = models.DateField(auto_now_add=True)
    ETA = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Shipping on {self.shipping_date}"

class SupplierPO(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    sup_approved = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Supplier PO - Approved: {self.sup_approved}"