from markdown2 import Markdown
from django.urls import reverse
import re

def link_gen(string):
	# Replace li:<link> with the link syntax in markdown
	def f(match):
		name = str(match.group('name'))
		return "[" + name + "](" + reverse('page',args=(name,)) + ")"
	return re.sub('li:(?P<name>\w+)', f, string)

def md(string):
	# Convert to markdown
	m = Markdown()
	return m.convert(string)

def process(string):
	proc = [link_gen, md]
	for f in proc:
		string = f(string)
	return string
