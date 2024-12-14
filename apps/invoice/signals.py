
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import InvoiceItem

@receiver([post_save, post_delete], sender=InvoiceItem)
def update_invoice_totals(sender, instance, **kwargs):
    invoice = instance.invoice
    
    # Recalculate total amounts
    total_net = sum(item.net_amount for item in invoice.items.all())
    total_tax = sum(item.tax_amount for item in invoice.items.all())
    
    # Update invoice totals
    invoice.total_net_amount = total_net
    invoice.total_tax_amount = total_tax
    invoice.total_amount = total_net + total_tax
    invoice.save()


