from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', HeroesHome.as_view(), name = 'home'),
    path('about/', about, name='about'),
    path('addarticle/', AddArticle.as_view(), name='add_article'),
    path('feedback/', ContactFormView.as_view(), name='feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', HeroesCategory.as_view(), name='category'),
]