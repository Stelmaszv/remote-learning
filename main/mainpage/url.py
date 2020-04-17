from django.urls import path
from mainpage.views import (main)
app_name = 'main'
urlpatterns = [
    path('', main.as_view(), name='start')
]
