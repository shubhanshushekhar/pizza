from django.shortcuts import render, get_object_or_404

from .models import Blog
import json
from django.http import HttpResponse
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def get_pizza(request, pizza_name):
    if request.method == 'GET':
        try:
            pizza = Blog.objects.get(pizza_name == title)
            response = json.dumps([{'Pizza Name': pizza.title, 'Pizza Shape': pizza.pizza_type, 'Pizza Toppings': pizza.summary }])
        except:
            response = json.dumps([{ 'Error': 'No car with that name'}])
    
    return HttpResponse(response, content_type='text/json')

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
