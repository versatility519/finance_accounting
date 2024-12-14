from django.urls import path
from django.conf.urls import include
from .views import (
    InvoiceListCreateView,
    InvoiceDetailView,
    
    InvoiceItemListCreateView,
    InvoiceItemDetailView,
    
    InvoiceDocListCreateView,
    InvoiceDocDetailView,
    
    TermsListCreateView,
    TermsDetailView,
    
    InvoiceNotesListCreateView,
    InvoiceNotesDetailView
    
)
urlpatterns = [
    path('invoices', include([
        path('', InvoiceListCreateView.as_view(), name='invoice-list-create'),
        path('/<int:pk>', InvoiceDetailView.as_view(), name='invoice-detail'),
    ])),
    
    path('invoice-item', include([
        path('', InvoiceItemListCreateView.as_view(), name='invoiceitem-list-create'),
        path('/<int:pk>', InvoiceItemDetailView.as_view(), name='invoiceitem-detail'),
    ])),
    
    path('invoice-doc', include([
        path('', InvoiceDocListCreateView.as_view(), name='invoicedoc-list-create'),
        path('/<int:pk>', InvoiceDocDetailView.as_view(), name='invoicedoc-detail'),
    ])),
    
    path('invoice-terms', include([
        path('', TermsListCreateView.as_view(), name='terms-list-create'),
        path('/<int:pk>', TermsDetailView.as_view(), name='terms-detail'),
    ])),
    
    path('invoice-notes', include([
        path('', InvoiceNotesListCreateView.as_view(), name='invoicenotes-list-create'),
        path('/<int:pk>', InvoiceNotesDetailView.as_view(), name='invoicenotes-detail'),
    ])),
]
