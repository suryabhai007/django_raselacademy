from django.core import serializers
import datetime
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from . forms import CommentForm
from django.shortcuts import render, get_object_or_404
from . models import Category, Blog, Comment

# Create your views here.

def index(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    try:
        
        blog_title = Blog.objects.filter(title__iexact=request.GET.get("title"))
    
    except Blog.DoesNotExist:
        return rendeer(request, "raselacademy/error.html", {"message": "No Blog Found"})
    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1

    num_visitor = request.session.get("num_visitor", 1)
    request.session["num_visitor"] = num_visitor + 1
    

    
    form = CommentForm(request.POST)
    if form.is_valid():

        comment = Comment()
        
       
        
        comment.author = form.cleaned_data['author']
        comment.body = form.cleaned_data['body']
        
        comment.save()
        return HttpResponseRedirect(reverse('success'))
        
        
        
    context = {
        "category": category,
        "blog_count": Blog.objects.all().count(),
        "blog": blog,
        "form": form,
        "blog_title": blog_title,
        "num_visits": num_visits,
        "now": datetime.datetime.now(),
        "num_visitor": num_visitor

        
        }
    
    return render(request, "raselacademy/index.html", context)

def blog_api(request):
    data = serializers.serialize("xml", Blog.objects.all())
    context = {
        "data": data
        }
    return render(request, "raselacademy/blog_api.html", context)




def blog(request, title):
    try:
        blog = Blog.objects.get(title=title)
    except Blog.DoesNotExist:
        return render(request, "raselacademy/error.html", {"message": "Blog Not Found"})
    
    form = CommentForm(request.POST)
    if form.is_valid():

        comment = Comment()
        
       
        
        comment.author = form.cleaned_data['author']
        comment.body = form.cleaned_data['body']
        
        comment.save()
        return HttpResponseRedirect(reverse('raselacademy:success'))
        
    context = {
        "blog": blog,
        "form": form
        
        }
    return render(request, "raselacademy/blog.html", context)



def categories(request, name):
    try:
        categories = Category.objects.get(name=name)
    except Category.DoesNotExist:
        raise Http404("Category Not Found")
    context = {
        "blog": categories.blog.all(),
        "categories": categories,
       
        }
    return render(request, "raselacademy/categories.html", context)




def success(request):
    return render(request, "raselacademy/success.html")




