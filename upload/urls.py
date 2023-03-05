from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.form_upload, name='upload_json'),
    path('upload/success/', views.upload_success, name='upload_success'),
]