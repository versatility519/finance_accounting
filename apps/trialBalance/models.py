from django.db import models
from apps.tAccount.models import TAccounts

# Create your models here.
class TrialBalance(models.Model):
    date = models.DateField()
    t_account = models.ForeignKey(TAccounts, on_delete=models.CASCADE)
    total_debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.account)
    
    def save(self, *args, **kwargs):
        # Update balance based on total debit and credit
        self.total_debit = sum(t.total_debit for t in TAccounts.objects.all())
        self.total_credit = sum(t.total_credit for t in TAccounts.objects.all())
        
        super().save(*args, **kwargs)
