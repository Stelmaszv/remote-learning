from django.contrib import admin
from django.urls import include, path
from . import views

from authorization.views import (register)
app_name = 'authorization'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', register.as_view()),
    path('accounts/',include('django.contrib.auth.urls')),
]
