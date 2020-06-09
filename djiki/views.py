from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db import IntegrityError
from .models import Content
from .utils import process


# Create your views here.
def index(request):
	return page(request, 'FrontPage')

def page(request, page_url):
	c = get_object_or_404(Content, url=page_url)
	context = {
		'text' : process(c.text),
		'url_': c.url,
		'title' : c.title,
		'last_edit' : c.last_edit.strftime('%Y-%m-%d %H:%M'),
	}
	return render(request, 'djiki/index.html', context)

def edit(request, page_url):
	c = get_object_or_404(Content, url=page_url)
	context = {
		'url_': c.url,
		'text' : c.text,
		'title' : c.title,
	}
	return render(request, 'djiki/edit.html', context)

def new(request):
	context = {
		'text' : '',
		'title' : '',
	}
	return render(request, 'djiki/new.html', context)

def submit_edit(request):
	page_url = request.POST['url']
	c = get_object_or_404(Content, url=page_url)
	c.text = request.POST['message']
	c.title = request.POST['title']
	c.save()
	return HttpResponseRedirect(reverse('page', args=(page_url,)))

def submit_new(request):
	url_ = request.POST['title'].replace(' ','')
	try:
		c = Content.objects.create(url = url_,
			title = request.POST['title'],
			text = request.POST['message'],
			)
	except IntegrityError:
		return HttpResponse("duplicate url or title, please change")
	else:
		c.save()
		return HttpResponseRedirect(
			reverse('page', args=(url_,))
			)
