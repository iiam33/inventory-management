from django.http import HttpResponse
from django.template import loader

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics

from .models import *
from .serializers import *

import httpx
import ast


def inventory_page(request):
    response = httpx.get("http://localhost:8000/api/inventory")
    json = response.json()
    data = {
        "inventory": json
    }
    template = loader.get_template('inventory_page.html')
    return HttpResponse(template.render(data, request))


class InventoryListAPIView(generics.ListAPIView):
    model = Inventory
    queryset = model.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "id"]


def inventory_detail_page(request, id):
    response = httpx.get(
        "http://localhost:8000/api/inventory", params={"id": id}).json()

    template = loader.get_template('inventory_detail_page.html')
    return HttpResponse(template.render(response[0], request))
