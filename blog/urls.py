from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('invate/', views.invate, name='invate'),
    path('invate/yes/', views.yes, name='yes'),
]

