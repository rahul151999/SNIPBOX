from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from snipboxconfig.permissions import IsOwner

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

class SnippetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific snippet by ID.
    GET: Retrieve the details of a specific snippet. Only the owner can access.
    PUT: Update the details of a specific snippet. Only the owner can update.
    DELETE: Delete a specific snippet. Only the owner can delete.
    The request body for PUT should include 'title', 'note', and optionally 'tags' (list of tag IDs).
    """
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = "id"
    http_method_names = ["get", "put", "pat" "delete"]

    def get_queryset(self):
        return Snippet.objects.filter(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        snippets = self.get_queryset()
        return Response(SnippetSerializer(snippets, many=True).data)

class SnippetBulkDeleteAPI(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        ids = request.data.get("ids", [])

        if not ids:
            return Response(
                {"error": "No IDs provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Snippet.objects.filter(
            id__in=ids,
            created_by=request.user
        ).delete()

        remaining = Snippet.objects.filter(created_by=request.user)

        serializer = SnippetSerializer(remaining, many=True)

        return Response({
            "message": "Selected snippets deleted",
            "remaining_snippets": serializer.data
        })