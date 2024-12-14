from django.urls import path
from .views import (
    TaxInfoListCreateView,
    TaxInfoDetailView,
    
    OrganizationListCreateView,
    OrganizationDetailView,
    
    DepartmentListCreateView,
    DepartmentDetailView,
)

urlpatterns = [ 
    path('tax-info', TaxInfoListCreateView.as_view(), name='taxinfo-list-create'),
    path('tax-info/<int:pk>', TaxInfoDetailView.as_view(), name='taxinfo-detail'),
    
    path('organization', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organization/<int:pk>', OrganizationDetailView.as_view(), name='organization-detail'),
    
    path('department', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('department/<int:pk>', DepartmentDetailView.as_view(), name='department-detail'),
]
