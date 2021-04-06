from django import forms
from django.forms import ModelForm
from .models import key_model

class home(forms.Form):
	name = forms.CharField(label='Name: ', max_length = 25)

class profile(forms.Form):
	name = forms.CharField(label='', max_length = 25)

class key(forms.ModelForm):
	class Meta: 
		model = key_model
		fields = ['keyName','keyDesc']
	
class this_week(forms.Form):
	name = forms.CharField(label='', max_length = 25)

class today(forms.Form):
	name = forms.CharField(label='', max_length = 25)