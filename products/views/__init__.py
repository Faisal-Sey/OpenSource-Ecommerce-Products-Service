
from django.http import HttpRequest
from django.shortcuts import render


# 404 page handler
def handler404(request: HttpRequest, exception: Exception):
    response = render(request, 'error_pages/404.html', {})
    response.status_code = 404
    return response