
from services.services import obj_all

def get_last_ten_photos(model, min_width):
    return model.objects.with_min_width(min_width)