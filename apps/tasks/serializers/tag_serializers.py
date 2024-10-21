from rest_framework import serializers

from apps.tasks.models.tag import Tag


class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = '__all__'