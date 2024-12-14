from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatementViewSet, StatementCategoryViewSet

router = DefaultRouter()
router.register(r'statements', StatementViewSet, basename='statement')
router.register(r'categories', StatementCategoryViewSet, basename='statement-category')


urlpatterns = [
    # path('statements', StatementViewSet.as_view(), name='statement'),
    # path('categories', StatementCategoryViewSet.as_view(), name='statement-category'),
    path('', include(router.urls)),
]

