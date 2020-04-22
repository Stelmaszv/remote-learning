from django import forms
from .models import (Lesson,Classroom)
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
             'teacher',
             'classroom',
             'subjects',
        ]