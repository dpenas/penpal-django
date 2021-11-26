from datetime import datetime 	
from django.db import models
from .modelsUser import User

# Would be better to use uuids instead of ids
class Message(models.Model):
	body = models.TextField()
	date = models.DateField(default=datetime.now, blank=True)
	from_user = models.ForeignKey(User, related_name="message_from_user", on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name="message_to_user", on_delete=models.CASCADE)

	def __str__(self):
		return "%s %s %s" % (self.from_user, self.to_user, self.body)