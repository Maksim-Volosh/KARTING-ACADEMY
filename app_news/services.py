from services.services import obj_all


def get_last_three_news(model):
    return obj_all(
        model=model,
        order_by=('-created_at',),
        only=('image',),
    )[:3]