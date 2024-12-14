
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BillItem

@receiver([post_save, post_delete], sender=BillItem)
def update_bill_totals(sender, instance, **kwargs):
    bill = instance.bill
    
    # Recalculate total amounts
    total_net = sum(item.net_amount for item in bill.items.all())
    total_tax = sum(item.tax_amount for item in bill.items.all())
    
    # Update bill totals
    bill.total_net_amount = total_net
    bill.total_tax_amount = total_tax
    bill.total_amount = total_net + total_tax
    
    bill.save()


