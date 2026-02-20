from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse

from .models import Snippet, Tag
from .serializers import SnippetSerializer


class SnippetListCreateAPI(generics.ListCreateAPIView):
    """
    API view to list and create snippets for the authenticated user.
    GET: List all snippets created by the authenticated user.
    POST: Create a new snippet for the authenticated user. 
    The request body should include 'title', 'note', and optionally 'tags' (list of tag IDs).
    """
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]

    def get_queryset(self):
        """Override to return only snippets created by the authenticated user."""
        return Snippet.objects.filter(created_by=self.request.user)
   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page or queryset, many=True)

        data = {
            "total_snippets": queryset.count(),
            "snippets": serializer.data
        }

        if page is not None:
            return self.get_paginated_response(data)

        return Response(data)

    def perform_create(self, serializer):
        """Override to set the created_by field to the authenticated user."""
        serializer.save(created_by=self.request.user)