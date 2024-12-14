# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import RequisitionItem, Requisition

@receiver([post_save, post_delete], sender=RequisitionItem)
def update_requisition_totals(sender, instance, **kwargs):
    requisition = instance.requisition
    
    # Recalculate total amounts
    total_net = sum(item.net_amount for item in requisition.items.all())
    total_tax = sum(item.tax_amount for item in requisition.items.all())
    
    # Update requisition totals
    requisition.total_net_amount = total_net
    requisition.total_tax_amount = total_tax
    requisition.total_amount = total_net + total_tax
    requisition.save()









# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django.db.models import Sum
# from .models import Requisition, RequisitionItem

# @receiver(post_save, sender=RequisitionItem)
# @receiver(post_delete, sender=RequisitionItem)
# def update_requisition_totals(sender, instance, **kwargs):
#     requisition = instance.requisition  # Reference the related requisition instance

#     # Recalculate total_net_amount as the sum of (quantity * price) across items
#     total_net = requisition.items.aggregate(
#         total_net=Sum("total_amount")
#     )['total_net'] or 0

#     # Recalculate total_tax_amount as the sum of tax_amount across items
#     total_tax = requisition.items.aggregate(
#         total_tax=Sum('tax_amount')
#     )['total_tax'] or 0

#     # Calculate total_amount as the sum of total_net and total_tax
#     total_amount = total_net + total_tax

#     # Update and save the requisition totals
#     requisition.total_net_amount = total_net
#     requisition.total_tax_amount = total_tax
#     requisition.total_amount = total_amount
#     requisition.save()
