from django.db import models

# Create your models here.
class key_model(models.Model):
	keyName = models.CharField(max_length = 25)
	keyDesc = models.CharField(max_length = 25)

class profile_model(models.Model):
	profileName =  models.CharField(max_length = 25)
	profileBio = models.CharField(max_length = 25)
	profileImage = models.ImageField(upload_to ='images/', null = True)