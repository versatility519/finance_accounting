from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import SubAccount

admin.site.register(SubAccount, MPTTModelAdmin)
