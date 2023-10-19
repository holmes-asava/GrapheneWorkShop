import uuid

from django.apps import apps
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import models
from django.db.models import Max, Q

from user_manager.models import User


class Post(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
