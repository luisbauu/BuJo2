from django import forms
from django.forms import ModelForm
from .models import *

class home(forms.Form):
	name = forms.CharField(label='Name: ', max_length = 25)

class profileFormName(forms.ModelForm):
	class Meta:
		model = profile_model
		fields = ['profileName']

class profileFormBio(forms.ModelForm):
	class Meta:
		model = profile_model
		fields = ['profileBio']

class profileFormImage(forms.ModelForm):
	class Meta:
		model = profile_model
		fields = ['profileImage']

class key(forms.ModelForm):
	class Meta: 
		model = key_model
		fields = ['keyName','keyDesc']
	
class this_week(forms.Form):
	name = forms.CharField(label='', max_length = 25)

class today(forms.ModelForm):
	class Meta:
		model = today_model
		fields = ['keyModel', 'todayDesc']