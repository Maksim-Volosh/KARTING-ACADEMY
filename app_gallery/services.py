
from services.services import obj_all

def get_last_ten_photos(model, min_width):
    return model.objects.with_min_width(min_width)[:10]

def get_all_photos(model, min_width=1080):
    return model.objects.with_min_width(min_width)