from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/', views.trae_contenido_json, name='file_json'),
    path('sse/', views.show_fight, name='pelea'),
]