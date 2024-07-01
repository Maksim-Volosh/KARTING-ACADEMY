def filter_decorator(func: callable):
    def filter_wrapper(model, filter=None, *args, **kwargs):
        result = func(model, *args, **kwargs)
        if filter:
            return result.filter(**filter)
        return result
    return filter_wrapper

def order_by_decorator(func: callable):
    def order_by_wrapper(model, order_by=(), *args, **kwargs):
        result = func(model, *args, **kwargs)
        if order_by:
            return result.order_by(*order_by)
        return result
    return order_by_wrapper

def select_related_decorator(func: callable):
    def select_related_wrapper(model, select_related=(), *args, **kwargs):
        result = func(model, *args, **kwargs)
        if select_related:
            return result.select_related(*select_related)
        return result
    return select_related_wrapper

def values_decorator(func: callable):
    def values_wrapper(model, values=(), *args, **kwargs):
        result = func(model, *args, **kwargs)
        if values:
            return result.values(*values)
        return result
    return values_wrapper

def only_decorator(func: callable):
    def only_wrapper(model, only=(), *args, **kwargs):
        result = func(model, *args, **kwargs)
        if only:
            return result.only(*only)
        return result
    return only_wrapper


def first_object_decorator(func: callable):
    def first_object_wrapper(model, first=False, *args, **kwargs):
        result = func(model, *args, **kwargs)
        if first:
            return result.first()
        return result
    return first_object_wrapper

@first_object_decorator
@only_decorator
@values_decorator
@select_related_decorator
@order_by_decorator
@filter_decorator
def obj_all(model):
    return model.objects.all()    

def obj_count(model):
    return model.objects.count()

"""
##How to use obj_all in your code, Here's an example of how to use the `obj_all` function:

def NameOfYourFunction(MODEL):
    return obj_all(
                model=MODEL,
                filter={'anyFIELD': anyVALUE},
                order_by=('anyFIELD',),
                select_related=('anyVALUE', 'anyVALUE',),
                values=('anyVALUE', 'anyVALUE', 'anyVALUE', 'anyVALUE', 'anyVALUE'),
                first=True or False,
            )
"""