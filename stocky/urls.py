from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .accounts import views as accounts_views
from .articles import views as articles_views

urlpatterns = [
    # articles
    path('', articles_views.articles, name='articles'),
    path('articles/', articles_views.articles, name='articles'),
    path('articles/add', articles_views.add_article, name='add_article'),
    path('articles/<int:article_id>', articles_views.article_details, name='article_details'),
    path('articles/delete/<int:article_pk>', articles_views.delete_article, name='delete_article'),
    path('articles/edit/<int:article_pk>', articles_views.edit_article, name='edit_article'),

    # accounts
    path('accounts/signup', accounts_views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='pages/accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
