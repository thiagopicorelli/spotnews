from rest_framework import serializers
from news.models import News
from news_rest.serializers import CategoriesSerializer

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "content", "author", "created_at", "image", "categories"]