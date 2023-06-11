from django import forms

from app.models import *


class User_Form(forms.ModelForm):
    class Meta():
        model=User
        fields=['username', 'email', 'password']
        widgets={'password':forms.PasswordInput}

class Question_Form(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question']
        widgets={'question':forms.Textarea(attrs={'cols':40, 'rows':4})}


class Answer_Form(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['question', 'answer']
        widgets={'answer':forms.Textarea(attrs={'cols':40, 'rows':4})}