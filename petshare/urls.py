from django.conf.urls import url, include
from django.urls import path
from .views import upload, vote

app_name = 'petshare'

urlpatterns = [
    path('', upload, name='upload'),
    path('vote/<int:pet>', vote, name='vote')
]
