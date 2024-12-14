from django.urls import path
from .views import (
    LedgerAccountCreateListView, LedgerAccountDetailView,
    SubAccountCreateListView, SubAccountDetailView
)

urlpatterns = [
    path('ledger-accounts', LedgerAccountCreateListView.as_view(), name='ledger-account-list'),
    path('ledger-accounts/<int:pk>', LedgerAccountDetailView.as_view(), name='ledger-account-detail'),
    
    path('sub-accounts', SubAccountCreateListView.as_view(), name='sub-account-lists'),
    path('sub-accounts/<int:pk>', SubAccountDetailView.as_view(), name='sub-account-lidetailsts')
]
