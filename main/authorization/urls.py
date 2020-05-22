from django.contrib import admin
from django.urls import include, path
app_name = 'authorization'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
]
