from django import forms
from .models import (Lesson,Classroom,Tasks,Dashbord)
from authorization.models import Account
class Lesson(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Lesson, self).__init__(*args, **kwargs)
        self.set()
    def set(self):
        self.fields['teacher'].queryset = Account.object.filter(email=self.email)
        self.fields['classroom'].queryset = Account.object.get(email=self.email).classrooms
        self.fields['subjects'].queryset = Account.object.get(email=self.email).is_teacher
    class Meta:
         model = Lesson
         fields = [
             'theme',
             'description',
             'taskfile',
             'teacher',
             'classroom',
             'subjects',
        ]
class AccountForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
         model = Account
         fields = [
             'subject',
             'message'
        ]
class TasksSolution(forms.ModelForm):
    class Meta:
         model = Tasks
         fields = [
             'taskfile'
        ]
class TasksSetRote(forms.ModelForm):
    class Meta:
         model = Tasks
         fields = [
             'rote'
        ]
class DashbordForm(forms.ModelForm):
    class Meta:
         model = Dashbord
         fields = [
             'theme',
             'description',
             'place'
        ]