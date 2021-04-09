from django.db import models
from django.shortcuts import render, reverse, redirect

# Create your models here.
class key_model(models.Model):
	keyName = models.CharField(max_length = 25)
	keyDesc = models.CharField(max_length = 100)

	def __str__(self):
		return self.keyName	

class profile_model(models.Model):
	profileName =  models.CharField(max_length = 25)
	profileBio = models.CharField(max_length = 25)
	profileImage = models.ImageField(upload_to ='images/', null = True)

class today_model(models.Model):
	keyModel = models.ForeignKey(key_model, on_delete = models.CASCADE)
	todayDesc = models.CharField(max_length=100)

	def today_edit(self):
		return reverse('new_today_update', args = [str(self.id)])

	def today_delete(self):
		return reverse('today_delete', args = [str(self.id)])


    # def deltwtask(self):
    #     return reverse('deletetwtask', args=[str(self.id)])
