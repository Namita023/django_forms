from django import forms
from app.models import *

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('Name is stating with a')
    
def check_for_len(value):
    if len(value)<4:
        raise forms.ValidationError('Length is less')

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    email=forms.EmailField()
    url=forms.URLField()

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    author=forms.CharField(max_length=100)
    date=forms.DateField()