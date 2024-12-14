from django.urls import path
from .views import (
    TAccountsDetailView, TAccountsListView,
    TAccountTransactionListView, TAccountTransactionDetailView
)

urlpatterns = [
    path('t-account', TAccountsListView.as_view(), name='t-account-list'),
    path('t-account/<int:pk>', TAccountsDetailView.as_view(), name='t-account-detail'),
    
    path('t-account-transaction', TAccountTransactionListView.as_view(), name='taccount-transaction-list'),
    path('t-account-transaction/<int:pk>', TAccountTransactionDetailView.as_view(), name='taccount-transaction-detail'),
]