
from services.services import obj_all


def get_last_ten_photos(model):
    return obj_all(
        model=model,
        order_by=('-created_at',),
        )[:10]