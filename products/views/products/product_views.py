from typing import Any, Dict

from django.db.models import Q, QuerySet
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
from products.utils.main import build_search_query, build_sort_key, paginate_data
from utils.logger.logger_handler import logger


class ProductListCreateAPIView(generics.ListCreateAPIView):  # type: ignore[misc]
    queryset = Product.objects.all().order_by("-created_on")
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
        products = super().get_queryset().filter(**filter_query).order_by(*order_by)
        logger.debug("Fetched products: %s", products.count())
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class ProductListAPIView(APIView):  # type: ignore[misc]
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        logger.debug("Fetching product list...")

        serializer = ProductSearchListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data: ProductSearchListDataType = serializer.validated_data
        logger.debug("Validated data: %s", data)

        query: str | None = data.get("query")
        custom_query: Dict[str, Any] | None = data.get("custom_query")
        reverse: bool | None = data.get("reverse")
        sort_key: str | None = data.get("sort_key")
        page_number: int | None = data.get("page_number")
        items_per_page: int | None = data.get("items_per_page")

        built_filter_query: Q = build_search_query(query or "", custom_query or {})
        logger.debug("Built filter query: %s", built_filter_query)

        built_sort_key = build_sort_key(sort_key or "", reverse or False)
        logger.debug("Built sort key: %s", built_sort_key)

        queryset: QuerySet[Product] = Product.objects.filter(
            built_filter_query
        ).order_by(built_sort_key)

        paginated_response = paginate_data(
            queryset, page_number or 1, items_per_page or 10
        )
        serializer = ListProductSerializer(paginated_response.get("data"), many=True)

        logger.debug("Fetched %d product items", queryset.count())
        return Response(data={**paginated_response, "data": serializer.data})
