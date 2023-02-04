from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from stocky.articles.forms import ArticleForm
from stocky.models import Article


@login_required(login_url='/accounts/login/')
def articles(request):
    all_articles = Article.objects.all()
    return render(request, 'pages/articles/index.html', {'articles': all_articles})


@login_required(login_url='/accounts/login/')
def article_details(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'pages/articles/article_details.html', {'article': article})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/articles')
    else:
        form = ArticleForm()
    return render(request, 'pages/articles/add-articles.html', {'form': form})


@login_required(login_url='/accounts/login/')
def edit_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = ArticleForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('/articles/{}'.format(article_pk))

    return render(request, 'pages/articles/edit-articles.html', {'form': form})


@login_required(login_url='/accounts/login/')
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('/articles')
