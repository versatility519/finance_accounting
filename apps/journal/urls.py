from django.urls import path
from .views import (
    # JournalCreateView,
    JournalListView, 
    JournalDetailView, 
    TransactionListView, 
    TransactionDetailView
)
urlpatterns = [
    # path('journalsAdd', JournalCreateView.as_view(), name='journal-create'),

    path('journal', JournalListView.as_view(), name='journal-list'),
    path('journal/<int:pk>', JournalDetailView.as_view(), name='journal-detail'),

    path('transaction', TransactionListView.as_view(), name='transaction-list'),
    path('transaction/<int:pk>', TransactionDetailView.as_view(), name='transaction-detail'),
]   