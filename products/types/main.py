from typing import Any, Dict, List, Literal, TypedDict


class ProductSearchListDataType(TypedDict):
    query: str
    custom_query: Dict[str, Any]
    page_number: int
    items_per_page: int
    reverse: bool
    sort_key: Literal["created_on", "price", "best_selling", "relevance"]


class ResponseDataType(TypedDict):
    status: str
    detail: str
    current_page: int
    total_data: int
    total_pages: int
    data: List[Any]
