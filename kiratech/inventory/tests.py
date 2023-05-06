from django.test import Client, TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework.views import status

from unittest import mock

from inventory.models import *
from inventory.serializers import *


class UnitTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.apiClient = APIClient()

        self.supplier1 = Supplier.objects.create(
            id = 1,
            name = "Supplier 1"
        )

        self.inventory1 = Inventory.objects.create(
            id=1,
            name="Inventory 1",
            description="inventory 1",
            note="inventory 1",
            stock=1,
            availability=True,
            supplier=self.supplier1
        )

    def test_inventory_page(self):
        url = reverse('inventory_page')
        response = self.apiClient.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_page.html')

    def test_inventory_list_view(self):
        url = reverse('inventory_list_view')
        response = self.apiClient.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        self.assertListEqual(response.data, serializer.data)

    def test_inventory_detail_page(self):
        url = reverse('inventory_detail_page', kwargs={'id': 1})
        response = self.apiClient.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_detail_page.html')
