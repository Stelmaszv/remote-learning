from django.urls import path
from ordinance.views import (add_person)
app_name = 'main'
urlpatterns = [
    path('addPerson/',add_person.as_view(),name="add_person"),
]
