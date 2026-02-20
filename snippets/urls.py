from django.urls import path

from snippets.views import SnippetListCreateAPI

urlpatterns = [
    path("snippets/", SnippetListCreateAPI.as_view()),
]