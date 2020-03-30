from django import forms
from .models import *

class Givebookform(forms.ModelForm):

     class Meta:
         model=Bookadd
         fields=['bookname','auther','language','genre','Bookadd_img','isbno','pageno']