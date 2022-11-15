from django.contrib.auth.models import User
from django.db import models
from django.db.models import *


class Article(Model):
    title = CharField(max_length=100)
    text = TextField()
    date_create = DateTimeField(auto_now_add=True)
    category = ForeignKey('Category', on_delete=CASCADE, null=True, blank=True)
    user = ForeignKey(User, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.title


class Category(Model):
    name_of_category = CharField(max_length=100)

    def __str__(self):
        return self.name_of_category
