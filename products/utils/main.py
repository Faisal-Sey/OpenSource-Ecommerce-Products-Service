from typing import Any

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet

from products.types.main import ResponseDataType


def paginate_data(
    data: QuerySet[Any], page_number: int, items_per_page: int = 10
) -> ResponseDataType:
    paginator = Paginator(data, items_per_page)

    try:
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page = paginator.page(1)

    total_data: int = data.count()

    total_pages: int = paginator.num_pages

    new_data = list(page)

    return {
        "status": "success",
        "detail": "Data fetched successfully",
        "current_page": page.number,
        "total_data": total_data,
        "total_pages": total_pages,
        "data": new_data,
    }
