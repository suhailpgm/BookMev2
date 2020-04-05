from django import forms
from .models import *

class chatform(forms.ModelForm):

     class Meta:
         model=Chat
         fields=['message']