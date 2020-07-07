from django.shortcuts import render
from django.http import Http404,JsonResponse
from .models import Tweet

# Create your views here.

def home_view(request, *agrs, **kwargs):
    return render(request,'pages/index.html',context={})
    

def tweet_list_view(request, *agrs, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{"id" : x.id, "content" : x.content} for x in qs]
    data = {
        "response" : tweet_list
    }
    return JsonResponse(data)


def tweet_view(request , twtnum, *agrs, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript
    return json data
    """
    data = {
        "id" : twtnum,
        #"image" = obj.image
    }
    status = 200
    try:
        obj = Tweet.objects.get(id = twtnum)
        data["content"] = obj.content
    except:
        data["message"] = 'Not Found'
        status = 404
        #raise Http404

    return  JsonResponse(data,status=status)

    #HttpResponse(f"<h1>This Is Home Page </h1>  </br> This Tweet Is number : { twtnum } --> {obj.content}")