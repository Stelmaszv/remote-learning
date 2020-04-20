from django import forms
from .models import (Classroom)
from authorization.models import Account
class educator(forms.ModelForm):
    class Meta:
         model = Account
         fields = [
             'email',
             'first_name',
             'last_name',
        ]