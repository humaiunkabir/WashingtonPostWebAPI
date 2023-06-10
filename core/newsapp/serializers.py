from rest_framework import serializers
from newsapp.models import NewsPost

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ("title", "content", "images")