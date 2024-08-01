from typing import Any, Dict, List

from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response

from products.models.products_model import Product
from products.serializers.product_serializer import (
    ListProductSerializer, SingleProductSerializer
)
from utils.logger.logger_handler import logger


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

    def get_queryset(self) -> Any:
        logger.debug("Fetching images list...")
        queryset = super().get_queryset()
        logger.debug("Fetched %d image items", queryset.count())
        return queryset


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = SingleProductSerializer

    def get_object(self) -> Product:
        image_id = self.kwargs.get('pk')
        logger.debug("Fetching images with ID %s...", image_id)
        image = super().get_object()
        logger.debug("Fetched images: %s", image)
        return image


class ProductRetrieveFilterAPIView(generics.ListCreateAPIView):
    queryset: QuerySet[Product] = Product.objects.all()
    serializer_class = ListProductSerializer

    def post(self, request, *args, **kwargs) -> Response:
        logger.debug("Fetching images with filter %s...")
        data: Dict[str, Any] = request.data
        filter_query: Dict[str, Any] = data.get("filter_query", {})
        order_by = data.get("order_by", ("-created_on",))
        images = super().get_queryset().filter(**filter_query).order_by(*order_by)
        logger.debug("Fetched images: %s", images.count())
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)
