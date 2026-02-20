from django.urls import path

from snippets.views import SnippetBulkDeleteAPI, SnippetListCreateAPI, SnippetRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("snippets/", SnippetListCreateAPI.as_view()),
    path("snippet/<int:id>", SnippetRetrieveUpdateDestroyAPIView.as_view(), name="snippet-detail"),
    path("snippets/delete/", SnippetBulkDeleteAPI.as_view(), name="snippet-bulk-delete")
]