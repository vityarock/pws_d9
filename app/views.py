from app.models import Post, Category
from app.serializers import PostSerializer, CatSerializer
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CatList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
