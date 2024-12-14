from django.core.exceptions import ValidationError
from django.db import models

from apps.users.models import CustomUser
from apps.account.models import LedgerAccount

from apps.project.models import Project

class OrderUnit(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IssueUnit(models.Model):
    name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
   
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Storeroom(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    storeroom = models.ForeignKey(Storeroom, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 

class Bin(models.Model):
    bin_name = models.CharField(max_length=100)
    bin_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.bin_name
    
class ReceptionDoc(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to='documents/reception')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class ReceptionItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_description = models.TextField()
    item_manufacturer = models.CharField(max_length=100)
    item_manufacturer_code = models.CharField(max_length=100)

    item_quantity = models.FloatField()
    item_bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name
    
class Reception(models.Model):
    po_number = models.PositiveIntegerField()
    items = models.ForeignKey('ReceptionItem',on_delete=models.CASCADE)
    notes = models.CharField(max_length=100)
    storekeeper = models.ForeignKey(
        CustomUser, 
        related_name='reception_as_storekeeper', 
        on_delete=models.CASCADE
    )
    recep_doc = models.ForeignKey('ReceptionDoc', on_delete=models.CASCADE)
    
    purchase_order = models.ForeignKey('purchaseOrder.PurchaseOrder', related_name='purchaseOrder', on_delete=models.CASCADE)
    
    date_received = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.notes    
    
class ReservationItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_description = models.TextField()
    item_manufacturer = models.CharField(max_length=100)
    item_manufacturer_code = models.CharField(max_length=100)
    item_quantity = models.FloatField()
    measureUnit = models.ForeignKey('IssueUnit', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancel', 'Cancelled'),
    ]
    
    items = models.ForeignKey('ReservationItem',on_delete=models.CASCADE)
    reserved_date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=100)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    reserved_by = models.ForeignKey(
        CustomUser, 
        related_name='reservation_as_reserved_by',
        on_delete=models.CASCADE
    )
    storekeeper = models.ForeignKey(
        CustomUser, 
        related_name='reservation_as_storekeeper',
        on_delete=models.CASCADE
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reason} - {self.reserved_date.strftime('%Y-%m-%d')}"

class IssueItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_description = models.TextField()
    item_manufacturer = models.CharField(max_length=100)
    item_manufacturer_code = models.CharField(max_length=100)
    item_quantity = models.FloatField()
    measureUnit = models.ForeignKey('IssueUnit', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name
    
class Issue(models.Model):
    name = models.CharField(max_length=100)
    
    items = models.ForeignKey('IssueItem',on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)

    storekeeper = models.ForeignKey(
        CustomUser,
        related_name='issue_as_storekeeper',
        on_delete=models.CASCADE
    )
    notes= models.TextField()
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.reason

class TransfertItem(models.Model):
    STATUS_CHOICES = [
        ('approve', 'Approve'),
        ('partially_approve', 'Partially Approve'),
        ('declined', 'Declined'),
    ]

    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_manufacturer = models.CharField(max_length=100)
    item_manufacturer_code = models.CharField(max_length=100)

    item_quantity = models.FloatField()

    item_bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name

class Transfert(models.Model):
    date = models.DateField()
    trans_number = models.CharField(max_length=20)
    trans_items = models.ForeignKey('TransfertItem', on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('approve', 'Approve'),
        ('transfered', 'Transfered')
    ])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.trans_number)
    
    def save(self, *args, **kwargs):
        self.trans_number = f"TRF-{self.trans_number}" 
        super().save(*args, **kwargs)


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    order_unit = models.ForeignKey('OrderUnit', on_delete=models.CASCADE)
    issue_unit = models.ForeignKey('IssueUnit', on_delete=models.CASCADE)
    
    preferred_supplier = models.ForeignKey(
        'supplier.Supplier',
        on_delete=models.CASCADE,
        related_name='preferred_inventory_items',
    )
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    
    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    
    price = models.DecimalField(max_digits=10, decimal_places=3)
    min_quantity = models.FloatField()
    max_quantity = models.FloatField()
    current_balance = models.FloatField()
    physical_count = models.FloatField()
    image = models.ImageField(upload_to='images/inventory_images/', blank=True, null=True)
    
    bin = models.ForeignKey('Bin', on_delete=models.CASCADE)
    
    reorder = models.BooleanField(default=False)
    reorder_point = models.FloatField()
    reorder_quantity = models.FloatField()
    
    type = models.CharField(
        max_length=100, 
        choices=[
            ('finished', 'Finished'), 
            ('unfinished', 'Unfinished')
        ]
    )
    
    suppliers = models.ForeignKey(
        'supplier.Supplier',
        on_delete=models.CASCADE,
        related_name='supplier_inventory_items',
    )

    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        """Custom validation to ensure reorder point and quantities are logical."""
        if self.reorder_point >= self.max_quantity:
            raise ValidationError('Reorder point must be less than max quantity.')
        if self.reorder_quantity <= 0:
            raise ValidationError('Reorder quantity must be a positive value.')