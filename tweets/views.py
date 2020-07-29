import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    """
    REST APT VIEW
    Consume by JavaScript (or React Native/Swift/Java/iOS/Android)
    return: JSON data
    """
    qs = Tweet.objects.all()  # query set
    tweets_list = [{"id": x.id, "content": x.content,
                    "likes": random.randint(0, 999)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST APT VIEW
    Consume by JavaScript (or React Native/Swift/Java/iOS/Android)
    return: JSON data
    """
    data = {
        "id": tweet_id,
    }

    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404  # page not found (Http 404)

    # json.dumps content_type="application/json"
    return JsonResponse(data, status=status)
