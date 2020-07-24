from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ArticleForm
from .models import Article, Tag
from .tasks import mul_2_numbers

def article_list(request):
    queryset = Article.objects.all()
    context = {
        "article_list": queryset
    }
    return render(request, "article/article_list.html", context)

def article_detail(request, id):
    try:
        art = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {
        "art": art
    }
    return render(request, "article/article_detail.html", context)

def tag_detail(request, name):
    tag = Tag.objects.get(title=name)
    context = {
        "tag": tag
    }
    return render(request, "article/tag_detail.html", context)

def article_create(request):
    init_data = {'title': ''}
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect()
    else:
        form = ArticleForm(initial=init_data)
    context = {'form': form}
    return render(request, "article/article_create.html", context)
