from django.db import models
from apps.journal.models import LedgerAccount

class StatementCategory(models.Model):
    category_name = models.CharField(max_length=100)
    accounts = models.ManyToManyField(LedgerAccount, related_name='statement_categories')
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = "Statement Categories"

class Statement(models.Model):
    date = models.DateField()
    statement_name = models.CharField(max_length=100)
    category = models.ForeignKey(StatementCategory, on_delete=models.CASCADE, related_name='statements')
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.statement_name} - {self.date}"
    
    class Meta:
        ordering = ['-date']
    
    