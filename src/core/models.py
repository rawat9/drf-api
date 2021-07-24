from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.title