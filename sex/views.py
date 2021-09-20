from django.urls import reverse
from . forms import CommentForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from . forms import CommentForm
from . models import Category, Blogger, Comment

# Create your views here.

def index(request):
    category = Category.objects.all()
    context = {
        "category": category
        }
    
    return render(request, "sex/index.html", context)


def category(request, name):
    try:
        category = Category.objects.get(name=name)
    except Category.DoesNotexist:
        raise Http404("No category found")
    context = {
        "category": category
        }
    return render(request, "sex/category.html", context)


def blogger(request, title):
    try:
        blogger = Blogger.objects.get(title=title)
    except Blogger.DoesNotExist:
        raise Http404("Blog not Found")
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = blogger.comment_set.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'], body = form.cleaned_data['body'])
        comment.save()
        request.session['sex']=True
        
        
        return HttpResponseRedirect(reverse('sex:comment', args=(blogger.title,)))
    return render(request, "sex/blog.html", {"form": form, "blogger": blogger})


def comment(request, title):
    try:
        blogger = Blogger.objects.get(title=title)
        comments = blogger.comment_set.filter(active=True)
    except Blogger.DoesNotExist:
        raise Http404("Not Found")
    context = {
        "blogger": blogger,
        "comments": comments
        }
    return render(request, "sex/comment.html", context)
        
            
       
   
                
                
                
