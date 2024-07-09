from django.shortcuts import render

from app_gallery.services import get_all_photos

from .models import Gallery
from services.services import obj_all

def gallery_list(request):
    context = {
        'gallery': get_all_photos(Gallery),
    }
    return render(request, 'gallery/gallery-list.html', context=context)
