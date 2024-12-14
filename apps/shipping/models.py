from django.db import models
from apps.sales.models import Sales
from django.core.validators import MinValueValidator

class ShippingItem(models.Model):
    item_name = models.CharField(
        max_length=100,
        help_text="Name of the shipped item"
    )
    description = models.CharField(
        max_length=100,
        help_text="Name of the shipped item"
    )
    manufacturer = models.CharField(
        max_length=100,
        help_text="Manufacturer of the shipped item"
    )
    manufacturer_code = models.CharField(
        max_length=100,
        help_text="Manufacturer code of the shipped item"
    )
    quantity = models.PositiveIntegerField(
        help_text="Quantity of items"
    )
    shipping = models.ForeignKey(
        'Shipping',
        on_delete=models.CASCADE,
        related_name='items'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.quantity})"

    class Meta:
        ordering = ['item_name']

class Shipping(models.Model):
    shipping_num = models.PositiveIntegerField(
        unique=True,
        validators=[MinValueValidator(1)],
        help_text="Unique shipping tracking number"
    )
    shipping_name = models.CharField(
        max_length=50,
        help_text="Name or description of the shipment"
    )
    shipping_date = models.DateField(
        help_text="Date when the shipment was sent"
    )
    other = models.CharField(
        max_length=20,
        choices=[
            ('transfer', 'Transfer'),
            ('others', 'Others'),
        ],
        help_text="Type of shipment"
    )
    notes = models.ForeignKey(
        'Notes',
        on_delete=models.CASCADE,
        related_name='shipments'
    )
    carrier = models.ForeignKey(
        'Carrier',
        on_delete=models.CASCADE,
        related_name='shipments'
    )
    sales = models.ForeignKey(
        Sales,
        on_delete=models.CASCADE,
        null=False,  # Ensure sales_id cannot be null
        blank=False  # Ensure sales_id is always provided
    )
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-shipping_date', '-created_at']
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shippings'

    def __str__(self):
        return f"Shipping #{self.shipping_num} - {self.shipping_name}"

    def clean(self):
        super().clean()
        # Add any custom validation here if needed

class Notes(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Title of the note"
    )
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.name

class Carrier(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the shipping carrier"
    )
    tracking_url = models.URLField(
        blank=True,
        help_text="Base URL for tracking shipments"
    )
    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Contact phone number for the carrier"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this carrier is currently available"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Carrier'
        verbose_name_plural = 'Carriers'

    def __str__(self):
        return self.name