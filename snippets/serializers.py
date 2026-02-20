from rest_framework import serializers
from .models import Snippet, Tag


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for Snippet model.
    This serializer converts Snippet model instances to JSON format and vice versa.
    It includes the 'id', 'title', 'note', 'tags', 'created_at', and 'updated_at' fields of the Snippet model.
    The 'tags' field is a write-only ListField that accepts a list of tag titles when creating or updating a Snippet.
    The serializer handles the creation of Tag instances and the association of tags with the Snippet during the create and update operations.
    """

    tags = serializers.ListField(write_only=True)
    tag_titles = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Snippet
        fields = [
            "id",
            "title",
            "note",
            "tags",
            "tag_titles",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
    
    def get_tag_titles(self, obj):
        return [tag.title for tag in obj.tags.all()]

    def create(self, validated_data):
        """
        Handle the creation of a Snippet instance, including the creation of Tag instances and 
        association with the Snippet.
        """
        tags_data = validated_data.pop("tags")
        snippet = Snippet.objects.create(**validated_data)

        for tag_title in tags_data:
            tag, _ = Tag.objects.get_or_create(title=tag_title)
            snippet.tags.add(tag)

        return snippet