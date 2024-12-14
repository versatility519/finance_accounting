from django.db import models

from apps.organization.models import Department
from apps.users.models import CustomUser
from apps.supplier.models import Supplier
from apps.organization.models import Tax
from apps.inventory.models import OrderUnit

class RequisitionDoc(models.Model):
    name = models.CharField(max_length=100)
    docs = models.FileField(upload_to='documents/requisition')
    requisition = models.ForeignKey('Requisition', related_name='requisition_docs', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class RequisitionItem(models.Model):
    requisition = models.ForeignKey('Requisition', related_name='items', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    measureUnit = models.ForeignKey(OrderUnit, on_delete=models.CASCADE)

    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    
    net_amount = models.DecimalField(max_digits=10, decimal_places=3, editable=False)

    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True, related_name='requisition_items')
    tax_amount = models.DecimalField(max_digits=10, decimal_places=3, editable=False)
    
    reception_quantity = models.DecimalField(max_digits=10, decimal_places=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.tax_group:
            self.tax_amount = self.quantity * self.price * self.tax_group.tax_rate
        else:
            self.tax_amount = 0
        self.net_amount = self.quantity * self.price
        super().save(*args, **kwargs)
    
class Requisition(models.Model):
    requisition_number = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)
    docs = models.ForeignKey(RequisitionDoc, on_delete=models.CASCADE, related_name='requisitiondocs')
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='approved_requisitions')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_requisitions')
    
    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=3, editable=False, null=True)
    total_net_amount = models.DecimalField(max_digits=10, decimal_places=3, editable=False, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3, editable=False, null=True)
    
    class Status(models.TextChoices):
        IN_PROGRESS = 'inProgress', 'In Progress'
        APPROVED = 'approved', 'Approved'
        CREATED = 'created', 'Created'
        REJECTED = 'rejected', 'Rejected'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancel', 'Cancel'

    status = models.CharField(max_length=20, choices=Status.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"Requisition #{self.requisition_number}"
    