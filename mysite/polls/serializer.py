from django.core import serializers
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['post_id','title','content','created_at']
  post_id = serializers.CharField(max_length=100)
  title = serializers.CharField(max_length=100)
  content = serializers.CharField(max_length=100)
  created_at = serializers.DateTimeField(input_formats=['%Y-%m-%d'])