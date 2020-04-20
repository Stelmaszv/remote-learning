from django import forms
from .models import (Classroom)
class UserAddpersonForm(forms.ModelForm):
    class Meta:
         model = Classroom
         fields = [
            'name'
        ]