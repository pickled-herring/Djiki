from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db import IntegrityError
from .models import Content, Edits
from .utils import process, diff


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

	c.edits_set.create(
		diff = diff(c.text, request.POST['message']),
		author = request.POST['author']
		)

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

def list_edits_all(request):
	return HttpResponse("listing all edits")

def list_edits(request, page_url):
	return HttpResponse("listing edits for page %s" % page_url)

def view_edit(request, edit_id):
	e = get_object_or_404(Edits, pk=edit_id)
	context = {
		'date' : e.date.strftime('%Y-%m-%d %H:%M'),
		'url_' : e.page.url,
		'diff' : e.diff.replace('\n','<br>'),
		'name' : e.author,
	}
	return render(request, 'djiki/view_edit.html', context)
