from django.db import models

# Create your models here.
class key_model(models.Model):
	keyName = models.CharField(max_length = 25)
	keyDesc = models.CharField(max_length = 25)
