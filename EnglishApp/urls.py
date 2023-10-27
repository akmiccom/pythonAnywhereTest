from django.urls import path
from EnglishApp.views import index


urlpatterns = [
    path('', index, name='index'),
]
