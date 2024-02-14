from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/detail.html', {'blog': blog})


def invate(request):
    return render(request, 'blog/invate.html')


def yes(request):
    return render(request, 'blog/yes.html')


# /home/sesshomaruu/django_pet/ source code 
# /home/sesshomaruu/django_pet/personal_portfolio/static/ static 
# 	/home/sesshomaruu/django_pet/media media 


# FORCE HTTPS ENABLED 

