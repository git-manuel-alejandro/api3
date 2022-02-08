from django.db import router
from rest_framework.routers import DefaultRouter
from posts.api.views import PostViewSet

router_post = DefaultRouter()

router_post.register(prefix='posts', basename='posts', viewset=PostViewSet)
