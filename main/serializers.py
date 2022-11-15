from rest_framework import serializers

from main.models import *


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'category', 'user']
