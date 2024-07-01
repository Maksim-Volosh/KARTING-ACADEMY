from services.services import obj_all


def get_partners(model):
    return obj_all(
        model=model,
        only=('logo', 'name', 'url'),
    )