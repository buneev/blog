from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import ArticleForm
from .models import Article, Tag


def article_list(request):
    queryset = Article.objects.all()
    context = {
        "article_list": queryset
    }
    return render(request, "article/article_list.html", context)


def article_detail(request, id):
    # art = get_object_or_404(Product, id=id)
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
    init_data = {
        'title': "This is my new article"
    }
    if request.method == "POST":
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            form.save()
            # return redirect()
    else:
        form = ArticleForm(initial=init_data)
    context = {
        'form': form
    }
    return render(request, "article/article_create.html", context)


def article_update(request, id=id):
    obj = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "article/article_create.html", context)


# TODO: Необходим рефакторинг
def article_delete(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)