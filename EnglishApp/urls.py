from django.urls import path
from EnglishApp.views import english


urlpatterns = [
    path('', english, name='english'),
]
