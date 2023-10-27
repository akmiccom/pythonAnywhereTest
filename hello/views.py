from django.shortcuts import render
from django.http import HttpResponse

html = '''
<h1>Hello World.</h1>
<h2>アップデートのテスト ➡ ファイルを直接修正</h2>
<h2>アップデートのテスト ➡ githubから修正</h2>
<h2>アップデートのテスト ➡ 構築を手動でやってみる</h2>
<h2>アップデートのテスト ➡ git pull</h2>
'''

def index(request):
    return HttpResponse(html)


