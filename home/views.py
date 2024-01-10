from django.shortcuts import render, redirect
from .models import BlogM
from .forms import CreateBlogForm
from django.http import HttpResponse

def Blog(reguest):
    blogs = BlogM.objects.all()
    context = {

        'blogs': blogs,
    }
    print(blogs)
    return render(reguest, 'home/Blog.html', context)


def createBlog(reguest):
    if reguest.method == 'POST':
        form = CreateBlogForm(reguest.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    form = CreateBlogForm
    context = {

            'form': form
    }
    return render(reguest, 'home/Create_Blog.html',context)


def deleteBlog(reguest,id):
    try:
        blog = BlogM.objects.get(pk=id)
        blog.delete()
    except:
        return HttpResponse(" не найдено!")
    return redirect('http://127.0.0.1:8000/')


