from django.shortcuts import render
from django.http import HttpResponse

html = '''
<h1>Hello World.</h1>
<h2>アップデーとのテストをしています</h2>
'''

def index(request):
    return HttpResponse(html)


