from app_partners.services import get_partners

from .models import Partner


def partners(request):
    partners = get_partners(Partner) 
    
    return {
        'partners': partners
    }