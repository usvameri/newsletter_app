from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home', views.homepage, name='homepage'),
    path('newsletters', views.newsletters, name='Newsletters'),
    path('newsletters/detail/<int:id>', views.newsletter_detail, name='newsletter_detail'),
    path('newsletters_json', views.newsletters_json, name='newsletters_json'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
