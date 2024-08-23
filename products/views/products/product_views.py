from typing import Any, Dict

from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.products.products_model import Product
from products.serializers.products.product_serializer import (
    ListProductSerializer,
    ProductSearchListSerializer,
    SingleProductSerializer,
)
from products.types.main import ProductSearchListDataType
from utils.logger.logger_handler import logger


class ProductListCreateAPIView(generics.ListCreateAPIView):  # type: ignore[misc]
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

    def get_queryset(self) -> Any:
        logger.debug("Fetching products list...")
        queryset = super().get_queryset()
        logger.debug("Fetched %d product items", queryset.count())
        return queryset


class ProductRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView  # type: ignore[misc]
):
    queryset = Product.objects.all()
    serializer_class = SingleProductSerializer

    def get_object(self) -> Product:
        product_id = self.kwargs.get("pk")
        logger.debug("Fetching product with ID %s...", product_id)
        product: Product = super().get_object()
        logger.debug("Fetched product: %s", product)
        return product


class ProductRetrieveFilterAPIView(generics.ListCreateAPIView):  # type: ignore[misc]
    queryset: QuerySet[Product] = Product.objects.all()
    serializer_class = ListProductSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        logger.debug("Fetching products with filter %s...")
        data: Dict[str, Any] = request.data
        filter_query: Dict[str, Any] = data.get("filter_query", {})
        order_by = data.get("order_by", ("-created_on",))
        images = super().get_queryset().filter(**filter_query).order_by(*order_by)
        logger.debug("Fetched products: %s", images.count())
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)


class ProductListAPIView(APIView):  # type: ignore[misc]
    @staticmethod
    def post(request: Request, *args: Any, **kwargs: Any) -> Response:
        logger.debug("Fetching product list...")

        serializer = ProductSearchListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data: ProductSearchListDataType = serializer.validated_data
        print(data)

        queryset = Product.objects.all()

        logger.debug("Fetched %d product items", queryset.count())
        return Response()
