from django.db import models

class LedgerAccount(models.Model):
    LEDGER_NAMES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ]
    
    ACCOUNT_TYPES = [
        ('debit', 'Debit'), 
        ('credit', 'Credit')
    ]
    
    TYPES_STATUS = [
        ('increase', 'Increase'), 
        ('decrease', 'Decrease')
    ]
    
    id = models.AutoField(primary_key=True)
    ledger_name = models.CharField(max_length=20, choices=LEDGER_NAMES) 
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    type_status = models.CharField(max_length=20, choices=TYPES_STATUS)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ledger_name  
 
class SubAccount(models.Model):
    # Each SubAccount has a name and can be linked to a parent SubAccount to allow nested structures.
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    ledger_account = models.ForeignKey(
        LedgerAccount,
        related_name='sub_accounts',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name

    class Meta:
        ordering = ['name']