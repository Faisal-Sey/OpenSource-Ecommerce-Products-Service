from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# 404 page handler
def handler404(request: HttpRequest, exception: Exception) -> HttpResponse:
    response = render(request, "error_pages/404.html", {})
    response.status_code = 404
    return response
