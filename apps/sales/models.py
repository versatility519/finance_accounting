from django.core.exceptions import ValidationError
from django.db import models
from apps.account.models import LedgerAccount
from apps.user.models import User
from apps.inventory.models import IssueUnit
from apps.organization.models import Tax, Department

class SalesItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    
    manufacturer = models.CharField(max_length=100)
    manufacturer_code = models.CharField(max_length=100)
    measure_unit = models.ForeignKey(IssueUnit, on_delete=models.CASCADE)

    item_code = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE)

    status = models.CharField(max_length=100, choices=[
        ('created', 'Created'),
        ('approved', 'Approved'),
        ('partially_received', 'Partially Received'),
        ('completed', 'Completed'),
    ])
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    sales = models.ForeignKey('Sales', related_name='items', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.item_name
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError('Quantity cannot be negative.')
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')
    
    def save(self, *args, **kwargs):
        print("Saving Sales Item...")
        if self.tax_group:
            self.tax_amount = self.quantity * self.price * self.tax_group.tax_rate
        else:
            self.tax_amount = 0
        self.net_amount = self.quantity * self.price
        super().save(*args, **kwargs)

class Sales(models.Model):
    sales_number = models.CharField(max_length=100)
    created_date = models.DateField()
    
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_sales')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_sales')
    
    status = models.CharField(max_length=20, choices=[
        ('created', 'Created'),
        ('approved', 'Approved'),
        ('sent', 'Sent'),
        ('partially_received', 'Partially Received'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ])
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    total_net_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.sales_number

    def save(self, *args, **kwargs):
        
        self.sales_number = f'SALES-{self.sales_number}'
        
        # Calculate total values based on related SalesItems
        self.total_net_amount = sum(item.net_amount for item in self.items.all())
        self.total_tax_amount = sum(item.tax_amount for item in self.items.all())
        self.total_amount = self.total_net_amount + self.total_tax_amount
        super().save(*args, **kwargs)
