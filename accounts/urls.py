from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('aboutus', views.aboutus, name='accounts/aboutus'),
    path('index', views.index, name='accounts/index'),
    path('news', views.news, name='accounts/news'),
    path('contact', views.contact, name='accounts/contact'),
    path('web', views.web, name='accounts/web')
]
