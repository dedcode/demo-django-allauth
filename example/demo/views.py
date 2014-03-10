from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import simplejson
from random import randrange


@login_required
def get_data(request):
    user = request.user
    data = getfacebook_data(user)
    return HttpResponse(data, mimetype="application/javascript")


def update_likes(user):
    try:
        from allauth.socialaccount.models import SocialToken, SocialAccount
        socialaccount = SocialAccount.objects.get(user=user)
        token = SocialToken.objects.get(account=socialaccount)

        from facepy import GraphAPI
        graph = GraphAPI(token)

        import datetime

        likes = graph.get('me/likes?limit=20')['data']
        return
    except Exception:
        pass