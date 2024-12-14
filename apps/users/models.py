from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.organization.models import Organization   

# Create your models here.
 
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('payabler', 'Payabler'),
        ('buyer', 'Buyer'),
        ('storekeeper', 'Storekeeper'),
        ('supplier', 'Supplier'),
        ('clients', 'Clients'),
    )
   
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    organization = models.ForeignKey(Organization, related_name='userOrganization', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.email
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.role
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='groupusers_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )