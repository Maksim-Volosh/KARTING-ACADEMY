from django.conf import settings
from django.shortcuts import redirect
from django.utils import translation


def set_language(request):
    language = request.GET.get('language')
    next_url = request.GET.get('next', '/')
    response = redirect(next_url)
    if language:
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
