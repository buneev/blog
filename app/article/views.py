from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import ArticleForm
from .models import Article


def article_create_view(request):
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


def article_update_view(request, id=id):
    obj = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "article/article_create.html", context)


def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "article/article_list.html", context)


def article_detail_view(request, id):
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


# TODO: Необходим рефакторинг
def article_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)