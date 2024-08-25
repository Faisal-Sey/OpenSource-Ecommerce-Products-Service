from typing import Any, Dict

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q, QuerySet

from config.project_configs import SORT_KEY_CHOICES
from products.types.main import ResponseDataType
from utils.logger.logger_handler import logger


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


def convert_dict_to_q_object(filters: Dict[str, Any]) -> Q:

    query = Q()

    for key, value in filters.items():
        query &= Q(**{key: value})

    return query


def build_search_query(query: str, custom_query: Dict[str, Any]) -> Q:
    logger.debug("Building query %s...")
    filter_query: Q = Q()

    if query:
        filter_query = Q(name__icontains=query) | Q(description__icontains=query)
    else:
        filter_query = convert_dict_to_q_object(custom_query)

    logger.debug("Built query: %s", filter_query)
    return filter_query


def build_sort_key(sort_key: str, reverse: bool = False) -> str:
    logger.debug("Building sort key %s...")
    modified_sort_key: str = sort_key
    if sort_key in ("best_selling", "relevance"):
        # TODO: Handle best selling and relevance sorting
        modified_sort_key = SORT_KEY_CHOICES[0]

    sort_operator: str = "-" if reverse else ""
    full_sort_key: str = f"{sort_operator}{modified_sort_key}"

    logger.debug("Built sort key: %s", full_sort_key)
    return full_sort_key
