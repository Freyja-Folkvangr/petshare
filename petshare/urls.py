from django.conf.urls import url, include
from django.urls import path
from .views import upload

app_name = 'petshare'

urlpatterns = [
    path('', upload, name='upload'),
]
