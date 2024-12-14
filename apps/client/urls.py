from django.urls import path
from .views import (
    ClientListCreateView,
    ClientDetailView,
    
    ContactListCreateView,
    ContactDetailView,
)
urlpatterns = [
    path('client', ClientListCreateView.as_view(), name='client-list-create'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client-detail'),
   
    path('contacts', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>', ContactDetailView.as_view(), name='contact-detail'),
]