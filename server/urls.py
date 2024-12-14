"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('apps.users.urls')),

    path('api/', include('apps.client.urls')),
    
    path('api/', include('apps.account.urls')),
    path('api/', include('apps.organization.urls')),
    path('api/', include('apps.supplier.urls')),

    path('api/', include('apps.project.urls')),

    path('api/', include('apps.invoice.urls')), 
    path('api/', include('apps.bill.urls')), 
    path('api/', include('apps.sales.urls')), 

    path('api/', include('apps.journal.urls')),
    path('api/', include('apps.inventory.urls')),
    path('api/', include('apps.requisition.urls')),
    
    path('api/', include('apps.production.urls')),
    path('api/', include('apps.purchaseOrder.urls')),
    
    path('api/', include('apps.tAccount.urls')),
    path('api/', include('apps.shipping.urls')),
    
    path('api/', include('apps.trialBalance.urls')),
    path('api/', include('apps.fiStatement.urls')),
]
