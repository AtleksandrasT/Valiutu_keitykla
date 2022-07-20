from django.urls import path, include
from .views import exchange


urlpatterns = [
    path('', exchange),
    path('i18n/', include('django.conf.urls.i18n')),
]