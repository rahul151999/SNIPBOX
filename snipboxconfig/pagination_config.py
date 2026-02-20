from rest_framework.pagination import PageNumberPagination

class SnippetPagination(PageNumberPagination):
    page_size = 10
