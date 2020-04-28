from django.urls import path
from ordinance.views import (add_Student,add_Personel,myStudents,myPersonel,addLesson,myLesson,ConfirmRecivedLesson,ShowLesson)
app_name = 'main'
urlpatterns = [
    path('addStudent/',add_Student.as_view(),name="addStudent"),
    path('addPersonel/',add_Personel.as_view(),name="addPersonel"),
    path('myStudents/',myStudents.as_view(),name="myStudents"),
    path('myPersonel/',myPersonel.as_view(),name="myPersonel"),
    path('addLesson/',addLesson.as_view(),name="addLesson"),
    path('myLesson/',myLesson.as_view(),name="myLesson"),
    path('ShowLesson/<int:id>',ShowLesson.as_view(),name="ShowLesson"),
    path('ConfirmRecivedLesson/<int:id>',ConfirmRecivedLesson.as_view(),name="ConfirmRecivedLesson"),
]
