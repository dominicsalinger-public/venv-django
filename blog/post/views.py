from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from models import Post

class IndexView(generic.ListView):
    template_name = 'post/index.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.order_by('-insert_date')