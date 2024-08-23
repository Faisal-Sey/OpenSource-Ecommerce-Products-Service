from typing import Any, List, Literal, TypedDict


class ProductSearchListDataType(TypedDict):
    query: str
    reverse: Literal["asc", "desc"]
    sort_key: Literal["name", "price", "rating"]


class ResponseDataType(TypedDict):
    status: str
    detail: str
    current_page: int
    total_data: int
    total_pages: int
    data: List[Any]
