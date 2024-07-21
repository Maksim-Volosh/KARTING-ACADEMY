from django.shortcuts import render

from app_gallery.services import get_all_photos
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Gallery
from services.services import obj_all

def gallery_list(request):
    gallery_list = get_all_photos(Gallery)
    
    paginator = Paginator(gallery_list, 15)
    page = request.GET.get('page')
    
    try:
        gallery = paginator.page(page)
    except PageNotAnInteger:
        gallery = paginator.page(1)
    except EmptyPage:
        gallery = paginator.page(paginator.num_pages)
    context = {
        'gallery': gallery,
    }
    return render(request, 'gallery/gallery-list.html', context=context)
