from .models import Club


def is_president(request):
    if request.user.is_authenticated:
        president_clubs = Club.objects.filter(president=request.user)
        
        if president_clubs.exists():
            return {'is_club_president': True, 'president_clubs': president_clubs}
    
    return {'is_club_president': False}
