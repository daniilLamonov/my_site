from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('works/', views.works, name='works'),
    path('main_app/', views.post_list, name='post_list'),
    path('contact/', views.contact, name='contact'),
]