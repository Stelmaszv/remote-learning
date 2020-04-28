from django.urls import path
from ordinance.views import (add_Student,add_Personel,myStudents,myPersonel,myTask,addLesson,myLesson,ConfirmRecivedLesson,ShowLesson,sentSolution,setRote)
app_name = 'main'
urlpatterns = [
    path('addStudent/',add_Student.as_view(),name="addStudent"),
    path('addPersonel/',add_Personel.as_view(),name="addPersonel"),
    path('myStudents/',myStudents.as_view(),name="myStudents"),
    path('myPersonel/',myPersonel.as_view(),name="myPersonel"),
    path('addLesson/',addLesson.as_view(),name="addLesson"),
    path('myLesson/',myLesson.as_view(),name="myLesson"),
    path('myTasks/',myTask.as_view(),name="myTasks"),
    path('ShowLesson/<int:id>',ShowLesson.as_view(),name="ShowLesson"),
    path('setRote/<int:id>',setRote.as_view(),name="setRote"),
    path('sentSolution/<int:id>/<int:lessonId>',sentSolution.as_view(),name="sentSolution"),
    path('ConfirmRecivedLesson/<int:id>',ConfirmRecivedLesson.as_view(),name="ConfirmRecivedLesson"),
]
