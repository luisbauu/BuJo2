from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from datetime import datetime
from .forms import home, profile, key, this_week, today
from .models import key_model

name = None
form = None

def page_home(request): 
	global name
	global form

	if name == None:
		if request.method == 'POST':
			form = home(request.POST)
			if form.is_valid():
				name = form.cleaned_data['name']
				return render(request, 'home.html', {'form' : form, 'name' : name})
		else:
			form = home()
			return render(request, 'home.html', {'form' : form})
	else:
		return render(request, 'home.html', {'form' : form, 'name' : name})

def page_profile(request):
	return render(request, 'profile.html')

def page_key(request):
	return render(request, 'key.html')

def page_this_week(request):
    return render(request, 'this_week.html')

def page_today(request):

    myDate = datetime.now()
    formattedDate = myDate.strftime("%m.%d.%A")
    
    return render(request, 'today.html', {'date': formattedDate})

class KeyListView(ListView):
	model = key_model
	template_name = 'key.html'
