from django.core.exceptions import ValidationError
from django.db import models

from apps.inventory.models import IssueUnit
from apps.client.models import Client, Contact
from apps.account.models import LedgerAccount
from apps.organization.models import Tax
from apps.user.models import User

class InvoiceDoc(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to='documents/invoices') 
    invoice = models.ForeignKey('Invoice', related_name='invoiceDocs', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
 
class Terms(models.Model):
    name = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', related_name='items', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    measure_unit = models.ForeignKey(IssueUnit, on_delete=models.CASCADE, related_name='invoice_items')
    
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE, related_name='invoice_items')
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
   
    net_amount = models.DecimalField(max_digits=10, decimal_places=3, editable=False)
    
    tax_group = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True, related_name='invoice_items')
    tax_amount = models.DecimalField(max_digits=10, decimal_places=3, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError('Quantity cannot be negative.')
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')
    
    def save(self, *args, **kwargs):
        print("Saving InvoiceItem...")
        if self.tax_group:
            self.tax_amount = self.quantity * self.price * self.tax_group.tax_rate
        else:
            self.tax_amount = 0
        self.net_amount = self.quantity * self.price
        super().save(*args, **kwargs)

class Invoice(models.Model):
    invoice_num = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    required_date = models.DateField()
       
    terms = models.ForeignKey('Terms', on_delete=models.CASCADE)
    ship_to = models.CharField(max_length=100)
    bill_to = models.CharField(max_length=100)

    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)  
    total_net_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
    turn_to_pdf = models.BooleanField(default=False)
    client_approval = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    
    class Status(models.TextChoices):
        NEED_APPROVAL = 'need approval', 'Need approval'
        APPROVED = 'approved', 'Approved'
        WAITING_PAYMENT = 'waiting payment', 'Waiting Payment'
        PAID = 'paid', 'Paid'
        COMPLETED = 'completed', 'Completed'
        CLOSE = 'close', 'Close'

    status = models.CharField(max_length=20, choices=Status.choices)

    def __str__(self):
        return str(self.invoice_num)
    
    def save(self, *args, **kwargs):

        self.invoice_num = f"INV-{self.invoice_num}" 

        # self.total_tax_amount = sum(item.tax_amount for item in self.items.invoiceItems.all())
        # self.total_net_amount = sum(item.total for item in self.items.invoiceItems.all())
        # self.total_amount = self.total_tax_amount + self.total_net_amount

        super().save(*args, **kwargs)
        
class InvoiceNotes(models.Model):
    notes = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='invoice_user', on_delete=models.CASCADE)
    invoice = models.ForeignKey('Invoice', related_name='notes', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.notes)