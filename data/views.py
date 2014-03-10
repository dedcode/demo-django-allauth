from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt

import oauth2 as oauth
import urlparse
import simplejson

@login_required
def get_fbdata(request):
    user = request.user
    print 'fetching data for: ' , user
    data = getfacebook_data(request)
    print 'success'
    return HttpResponse(data, mimetype="application/javascript")


def getfacebook_data(request):
    user = request.user
    print 'hello', user
    try:
        from allauth.socialaccount.models import SocialToken, SocialAccount
        print 'from ->', SocialAccount.objects.all()
        socialaccount = SocialAccount.objects.get(user=user, provider = 'facebook')
        print 'socialaccount'
        token = SocialToken.objects.get(account=socialaccount)
        print 'token'
        print socialaccount, token

        from facepy import GraphAPI
        graph = GraphAPI(token)
        print graph
        import datetime

        friends = graph.get('me/friends')['data']
        print friends
        return HttpResponse(friends, mimetype="application/javascript")

    except Exception:
    	print 'failure'
        pass


def getlinkedin_data(request):
    user = request.user
    print 'hello', user
    # Use your credentials to build the oauth client
    consumer = oauth.Consumer(key="", secret="")

    # get the token
    from allauth.socialaccount.models import SocialToken, SocialAccount
    socialaccount = SocialAccount.objects.get(user=user, provider = 'linkedin')
    token = SocialToken.objects.get(account=socialaccount)
    print token
    print consumer

    token = oauth.Token(key="", secret="")
    client = oauth.Client(consumer, token)

    # Fetch first degree connections
    resp, content = client.request('http://api.linkedin.com/v1/people/~/connections?format=json')
    results = simplejson.loads(content)    
    
    print results
    return HttpResponse(content, mimetype="application/javascript")
