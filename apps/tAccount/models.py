from django.db import models
from decimal import Decimal
from apps.account.models import LedgerAccount
from apps.journal.models import Transaction

from django.db import models
from django.core.exceptions import ValidationError

class TAccountTransaction(models.Model):
    date = models.DateField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='t_account_transactions')
    transaction_account = models.CharField(max_length=50) 
    debit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.transaction:
            raise ValidationError("Transaction must be specified.")
        
        self.transaction_account = self.transaction.account.ledger_name
        
        if self.transaction.t_type == "credit":
            self.credit_amount = self.transaction.t_amount 
            self.debit_amount = Decimal(0.00)
        elif self.transaction.t_type == "debit":
            self.debit_amount = self.transaction.t_amount
            self.credit_amount = Decimal(0.00)
        else:
            raise ValueError("Invalid transaction type; must be 'credit' or 'debit'")
        
        if self.debit_amount < 0 or self.credit_amount < 0:
            raise ValidationError("Debit and credit amounts must be non-negative.")

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"TAccountTransaction {self.id} - Transaction: {self.transaction.id}"
    
class TAccounts(models.Model):
    account = models.ForeignKey(LedgerAccount, on_delete=models.CASCADE)
    transaction = models.ForeignKey(TAccountTransaction, on_delete=models.CASCADE)
    total_debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.account)
    
    def save(self, *args, **kwargs):
        # Update balance based on total debit and credit
        self.total_debit = sum(t.debit_amount for t in TAccountTransaction.objects.all())
        self.total_credit = sum(t.credit_amount for t in TAccountTransaction.objects.all())
        
        self.balance = self.total_debit - self.total_credit
        super().save(*args, **kwargs)
