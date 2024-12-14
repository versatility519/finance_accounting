from django.urls import include, path
from .views import (
    LegerAccountListCreateView,
    LegerAccountDetailView,
    
    SubSAccountListCreateView,
    SubSAccountDetailView,
 
    SubOneAccountListCreateView,
    SubOneAccountDetailView,
    
    SubTwoAccountListCreateView,
    SubTwoAccountDetailView,
    
    SubThreeAccountListCreateView,
    SubThreeAccountDetailView
    
)

urlpatterns = [
    path('leger-account', LegerAccountListCreateView.as_view(), name='supplier-list-create'),
    path('leger-account/<int:pk>', LegerAccountDetailView.as_view(), name='supplier-detail'),
    
    path('subs-account', SubSAccountListCreateView.as_view(), name='subaccount-list-create'),
    path('subs-account/<int:pk>', SubSAccountDetailView.as_view(), name='subaccount-detail'),
    
    path('onelayer-account', SubOneAccountListCreateView.as_view(), name='subone-list-create'),
    path('onelayer-account/<int:pk>', SubOneAccountDetailView.as_view(), name='subone-detail'),
    
    path('twolayer-account', SubTwoAccountListCreateView.as_view(), name='subtwo-list-create'),
    path('twolayer-account/<int:pk>', SubTwoAccountDetailView.as_view(), name='subtwo-detail'),
    
    path('threelayer-account', SubThreeAccountListCreateView.as_view(), name='subthree-list-create'),
    path('threelayer-account/<int:pk>', SubThreeAccountDetailView.as_view(), name='subthree-detail'),
    
]