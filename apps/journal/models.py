from django.db import models
from apps.account.models import LedgerAccount

# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    s_date = models.DateField(auto_now_add=True)   
    e_date = models.DateField(null=True, blank=True)  
    number = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_credit(self):
        return sum(transaction.t_amount for transaction in self.transactions.filter(t_type='credit'))

    @property 
    def total_debit(self):
        return sum(transaction.t_amount for transaction in self.transactions.filter(t_type='debit'))
    
    def __str__(self):
        return self.name
    
    
class Transaction(models.Model):
    t_name = models.CharField(max_length=100)
    t_date = models.DateField(auto_now_add=True)   
    t_amount = models.DecimalField(max_digits=10, decimal_places=2)  
    t_description = models.TextField(max_length=200)
    t_type = models.CharField(max_length=7, choices=[
        ('debit', 'Debit'),
        ('credit', 'Credit')
    ])
    account = models.ForeignKey(LedgerAccount, related_name='transactions', on_delete=models.CASCADE)  
    journal = models.ForeignKey('Journal', related_name='transactions', on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.t_name