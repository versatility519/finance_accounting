from django.urls import path
from .views import (
    TrialBalanceListCreateView,
    TrialBalanceDetailView
)

urlpatterns = [
    # Trial Balance endpoints
    path('trial-balance', TrialBalanceListCreateView.as_view(), name='trial-balance-list'),
    path('trial-balance/<int:pk>', TrialBalanceDetailView.as_view(), name='trial-balance-detail'),
]
