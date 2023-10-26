from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World.</h1>')


# e5e9312609a5b2f798379328df4104a1bfb287cb
# https://github.com/akmiccom/pythonAnywhereTest.git

# pip3.10 install --user pythonanywhere
# pa_autoconfigure_django.py --python=3.10 https://github.com/akmiccom/pythonAnywhereTest.git
# https://tutorial.djangogirls.org/ja/deploy/