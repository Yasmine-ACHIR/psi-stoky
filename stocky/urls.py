from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .accounts import views as accounts_views

urlpatterns = [
    path('', views.categories),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('accounts/signup', accounts_views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='pages/accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout')
]
