from datetime import datetime 	
from django.db import models

# Would be better to use uuids instead of ids
class User(models.Model):
	email = models.EmailField(max_length=254)
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.email