from rest_framework import serializers


class RepositorioSerializer(serializers.Serializer):
    url = serializers.URLField()