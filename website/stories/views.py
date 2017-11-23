from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Story

def index(request):
    latest_stories = Story.objects.order_by('-insert_date')[:5]
    context = {
        'latest_stories':latest_stories
    }
    return render(request, 'website/index.html', context)

def detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    context = {'story': story}
    return render(request, 'website/story.html', context)