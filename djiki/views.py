from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Content


# Create your views here.
def index(request):
	c = Content.objects.get(pk=1)
	context = {
		'text' : c.text,
		'last_edit' : c.last_edit.strftime('%Y-%m-%d %H:%M'),
	}
	return render(request, 'djiki/index.html', context)

def edit(request):
	c = Content.objects.get(pk=1)
	context = {
		'text' : c.text,
	}
	return render(request, 'djiki/edit.html', context)

def submit(request):
	c = Content.objects.get(pk=1)
	c.text = request.POST['message']
	c.save()
	return HttpResponseRedirect(reverse('index'))
