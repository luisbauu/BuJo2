from django import forms

class home(forms.Form):
	name = forms.CharField(label='Name: ', max_length = 25)

class profile(forms.Form):
	name = forms.CharField(label='', max_length = 25)

class key(forms.Form):
	name = forms.CharField(label='', max_length = 25)

class this_week(forms.Form):
	name = forms.CharField(label='', max_length = 25)

class today(forms.Form):
	name = forms.CharField(label='', max_length = 25)