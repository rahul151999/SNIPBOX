from rest_framework import serializers
from .models import Snippet, Tag

class BaseSnippetSerializer(serializers.ModelSerializer):
    """Base serializer for Snippet model to be used by both overview and detail serializers."""
    tag_titles = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Snippet
        fields = [
            "id",
            "title",
            "note",
            "tag_titles",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def get_tag_titles(self, obj):
        return [tag.title for tag in obj.tags.all()]

class SnippetOverviewSerializer(BaseSnippetSerializer):
    """
    Serializer for listing snippets with a detail URL. 
    This serializer is used for the overview endpoint to provide a summary of each snippet 
    along with a URL to access its details.
    """
    detail_url = serializers.SerializerMethodField()

    class Meta(BaseSnippetSerializer.Meta):
        fields = BaseSnippetSerializer.Meta.fields + ["detail_url"]

    def get_detail_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/api/snippet/{obj.id}")


class SnippetSerializer(BaseSnippetSerializer):
    """
    Serializer for creating and updating snippets. 
    This serializer includes a write-only field for tags, 
    which accepts a list of tag titles to associate with the snippet.
    """
    tags = serializers.ListField(write_only=True)

    class Meta(BaseSnippetSerializer.Meta):
        fields = BaseSnippetSerializer.Meta.fields + ["tags"]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        snippet = Snippet.objects.create(**validated_data)

        for tag_title in tags_data:
            tag, _ = Tag.objects.get_or_create(title=tag_title)
            snippet.tags.add(tag)

        return snippet

class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tag model.
    This serializer converts Tag model instances to JSON format and vice versa.
    It includes the 'id' and 'title' fields of the Tag model.
    """

    class Meta:
        model = Tag
        fields = ["id", "title"]