from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView
from datetime import datetime
from .forms import *
#from .forms import home, key, this_week, today,profileFormName, profileFormBio, profileFormImage
from .models import *

name = None
form = None

def page_home(request): 
	global name

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
		return render(request, 'home.html', {'name' : name})

def page_profile(request):
	return render(request, 'profile.html')

def page_key(request):
	return render(request, 'key.html')

def page_this_week(request):
    return render(request, 'this_week.html')

def new_today(request):
	form = today()
	if request.method == 'POST':
		form = today(request.POST)
		if form.is_valid():
			form.save()
			return redirect('today')
	return render(request,'update.html', {'form' : form})

def new_thisWeek(request):
	form = this_week()
	if request.method == 'POST':
		form = this_week(request.POST)
		if form.is_valid():
			form.save()
			return redirect('this_week')
	return render(request,'update.html', {'form' : form})

def new_key(request):
	form = key()
	if request.method == 'POST':
		form = key(request.POST)
		if form.is_valid():
			form.save()
			return redirect('key')
	return render(request,'update.html', {'form' : form})

def page_today_done(request,pk):
	done = today_model.objects.get(id = pk)
	done.keyModel = key_model.objects.get(id = 30)
	done.save()
	return redirect('today')

def page_thisWeek_done(request,pk):
	done = thisWeek_model.objects.get(id = pk)
	done.keyModel = key_model.objects.get(id = 30)
	done.save()
	return redirect('this_week')

def page_today(request):

    myDate = datetime.now()
    formattedDate = myDate.strftime("%m.%d.%A")
    
    return render(request, 'today.html', {'date': formattedDate})
################
class KeyListView(ListView):
	model = key_model
	template_name = 'key.html'
################
class ProfileDetailView(DetailView):
	model = profile_model
	template_name = 'profile.html'

	def get_object(self):
		return profile_model.objects.first()

class ProfileNameView(UpdateView):
	model = profile_model
	template_name = 'update.html'
	form_class = profileFormName

	def get_object(self):
		return profile_model.objects.first()

	def get_success_url(self):
		return reverse('profile')

class ProfileBioView(UpdateView):
	model = profile_model
	template_name = 'update.html'
	form_class = profileFormBio

	def get_object(self):
		return profile_model.objects.first()

	def get_success_url(self):
		return reverse('profile')

class ProfileImageView(UpdateView):
	model = profile_model
	template_name = 'update.html'
	form_class = profileFormImage

	def get_object(self):
		return profile_model.objects.first()

	def get_success_url(self):
		return reverse('profile')
################
class TodayListView(ListView):
	model = today_model
	template_name = 'today.html'

class TodayUpdateView(UpdateView):
	model = today_model
	template_name =  'update.html'
	form_class = today

	def get_success_url(self):
		return reverse('today')

class TodayDeleteView(DeleteView):
	model = today_model
	template_name =  'delete.html'
	form_class = today

	def get_success_url(self):
		return reverse('today')
################
class thisWeekListView(ListView):
	model = thisWeek_model
	template_name = 'this_week.html'

class thisWeekUpdateView(UpdateView):
	model = thisWeek_model
	template_name =  'update.html'
	form_class = this_week

	def get_success_url(self):
		return reverse('this_week')

class thisWeekDeleteView(DeleteView):
	model = thisWeek_model
	template_name =  'delete2.html'
	form_class = this_week

	def get_success_url(self):
		return reverse('this_week')
