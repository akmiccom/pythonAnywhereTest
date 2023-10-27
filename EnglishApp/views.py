from django.shortcuts import render
from django.http import HttpResponse

import markdown

filepath = 'EnglishApp\markdown\ネイティブなら6歳までに覚える英語の型.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

extentions = [
    'extra',
    'toc',
    ]

extension_configs = {
    'toc': {
        'title': 'Table of Contents', # 文字のタイトル
        'baselevel': 1, # 目次の開始時のheader
        'toc_depth': 1, # header のいくつまで表示するか
        }
    }

html = markdown.markdown(
    text,
    extensions=extentions,
    extension_configs=extension_configs,
    )

def english(request):
    return HttpResponse(html)