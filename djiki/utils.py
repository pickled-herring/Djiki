from markdown2 import Markdown

def preprocess(string):
	md = Markdown()
	return md.convert(string)
