from django.urls import path

from snippets.views import SnippetBulkDeleteAPI, SnippetListCreateAPI, SnippetRetrieveUpdateDestroyAPIView, TagDetailAPI, TagListAPI

urlpatterns = [
    path("snippets/", SnippetListCreateAPI.as_view()),
    path("snippet/<int:id>", SnippetRetrieveUpdateDestroyAPIView.as_view(), name="snippet-detail"),
    path("snippets/delete/", SnippetBulkDeleteAPI.as_view(), name="snippet-bulk-delete"),
    path("tags/", TagListAPI.as_view()),
    path("tags/<int:pk>/", TagDetailAPI.as_view()),
]