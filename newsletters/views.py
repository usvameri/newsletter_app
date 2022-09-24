from django.shortcuts import render
from newsletterdb.models import Newsletter
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def newsletters(request):
    data = {
        'newsletters': Newsletter.objects.all()
    }
    return render(request, 'newsletters.html', data)


def newsletter_detail(request, id):
    data = {
        'newsletter': Newsletter.objects.get(id=id)
    }
    return render(request, 'newsletter_detail.html', data)


def newsletters_json(request):
    data = list(Newsletter.objects.all())
    data = serializers.serialize('json', data)
    # return JsonResponse(data, safe=False)
    return HttpResponse(data, content_type='application/json')

