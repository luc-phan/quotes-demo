from rest_framework import serializers
from .models import Quote, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class QuoteSerializer(serializers.ModelSerializer):
    # We display the tag names instead of just IDs
    tags = TagSerializer(many=True, read_only=True)
    # We display the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'created_at', 'owner', 'tags']
