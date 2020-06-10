from django.db import models

# Create your models here.
class Content(models.Model):
	text = models.TextField();
	url = models.CharField(max_length=256, unique=True);
	title = models.CharField(max_length=256, unique=True);
	last_edit = models.DateTimeField(auto_now=True);

class Edits(models.Model):
	page = models.ForeignKey(Content, on_delete=models.CASCADE)
	diff = models.TextField();
	date = models.DateTimeField(auto_now=True);
	author = models.CharField(max_length=256)
