from django.shortcuts import render
from django.http import HttpResponse

html = '''
<h1>Hello World.</h1>
<h2>アップデーとのテスト ➡ ファイルを直接修正</h2>
<h2>アップデーとのテスト ➡ githubから修正</h2>
<h2>アップデーとのテスト ➡ 構築を手動でやってみる</h2>
'''

def index(request):
    return HttpResponse(html)


