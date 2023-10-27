from django.shortcuts import render
from django.http import HttpResponse

html = '''
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
    <h1>Hello World.</h1>
    <h2>アップデートのテスト ➡ ファイルを直接修正</h2>
    <h2>アップデートのテスト ➡ githubから修正</h2>
    <h2>アップデートのテスト ➡ 構築を手動でやってみる</h2>
    <h2>アップデートのテスト ➡ git pull</h2>
        <div>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My first post</a></h2>
            <p>Aenean eu leo quam. こんにちは！ よろしくお願いします！ </p>
        </div>

        <div>
            <p>公開日: 2014/06/14, 12:14</p>
            <h2><a href="">2番目の投稿</a></h2>
            <p> こんにちは！ よろしくお願いします！ </p>
        </div>
    </body>
</html>
'''

def index(request):
    return HttpResponse(html)


