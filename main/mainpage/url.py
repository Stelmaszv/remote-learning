from django.urls import path
from mainpage.views import (main)
from django.conf.urls.static import static
from django.conf import settings
app_name = 'main'
urlpatterns = [
    path('', main.as_view(),name='Start')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
