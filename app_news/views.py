from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from app_news.models import News
from services.services import obj_all

def news_list(request):
    news_list = obj_all(News)
    
    paginator = Paginator(news_list, 15)
    page = request.GET.get('page')
    
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'news': news,
    }
    return render(request, 'news/news-list.html', context=context)

def news_detail(request, nid):
    news = obj_all(News, filter={'id': nid}, first=True)
    context = {
        'news': news,
    }
    print(obj_all(News, filter={'id': nid},))
    return render(request, 'news/news-detail.html', context=context)
