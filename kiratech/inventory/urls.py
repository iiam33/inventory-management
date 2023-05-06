from django.urls import path

from .views import *

urlpatterns = [
    path('inventory', inventory_page,
         name='inventory_page'),
    path('api/inventory', InventoryListAPIView.as_view(),
         name='inventory_list_view'),
    path('inventory/<int:id>', inventory_detail_page, name='inventory_detail_page')
]
