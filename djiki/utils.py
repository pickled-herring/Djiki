from markdown2 import Markdown
from django.urls import reverse
import re
import difflib
from html import escape

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
	proc = [escape, link_gen, md]
	for f in proc:
		string = f(string)
	return string

def diff(string1, string2):
	# generate diff between 2 strings
	lines_1 = string1.splitlines()
	lines_2 = string2.splitlines()
	diff = difflib.unified_diff(lines_1, lines_2, lineterm='')
	return '\n'.join(list(diff))
