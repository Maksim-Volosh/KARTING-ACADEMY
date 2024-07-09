from django.shortcuts import render

from app_news.models import News
from services.services import obj_all

def news_list(request):
    context = {
        'news': obj_all(News),
    }
    return render(request, 'news/news-list.html', context=context)

def news_detail(request, nid):
    news = obj_all(News, filter={'id': nid}, first=True)
    context = {
        'news': news,
    }
    print(obj_all(News, filter={'id': nid},))
    return render(request, 'news/news-detail.html', context=context)
