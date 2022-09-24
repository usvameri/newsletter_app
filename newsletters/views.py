from django.shortcuts import render
from newsletterdb.models import Newsletter
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

