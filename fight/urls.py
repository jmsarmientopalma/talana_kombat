from django.urls import path

from . import views

urlpatterns = [
    path('sse/', views.show_fight, name='pelea')
]