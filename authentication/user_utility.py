from management.models import Club


def check_user_club_level(user, club):
    if user in club.sponsors:
        return "sponsor"

    if user in club.officers:
        return "officer"

    if user in club.members:
        return "member"

    return "none"


def is_club_sponsor(user):
    clubs = Club.objects.all()
    for club in clubs:
        if user in club.sponsors.all():
            return club.name
    return "None"
#         LEFT OFF HERE, write this method so that we check if the user trying to login is is a sponsor in any of all clubs, and if he is he should be shown a MY CLUBS page instead of all clubs
