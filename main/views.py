from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.viewsets import *

from main.models import *
from main.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from main.serializers import ArticleSerializer


# class ArticleAPIView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class ArticleUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # permission_classes = (IsOwnerOrReadOnly,)
#     permission_classes = (IsAuthenticated,)
#
#
# class ArticleDeleteAPIView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsAdminUser,)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminUser,)
