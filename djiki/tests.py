from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Content
from .utils import process, diff

# Create your tests here.

def submit_post(s, page, data):
	return s.client.post(reverse(page), data, follow=True)

class ViewTests(TestCase):
	def setUp(self):
		return Content.objects.create(url='FrontPage',
			title = 'Front page',
			text = "Welcome to the front page",
			)

	def test_views(self):
		def test_(page, code, args):
			response = self.client.get(reverse(page, args=args))
			self.assertEqual(response.status_code, code)

			test_('index', 200, ())
			test_('page', 200, ('FrontPage',))
			test_('edit', 200, ('FrontPage',))
			test_('page', 404, ('f',))
			test_('edit', 404, ('f',))
			test_('new', 200, ())

	def test_edit(self):
		data = {
			'url':'FrontPage',
			'title':'Front page',
			'message':'I have now changed the front page',
			'author':'harry',
		}

		response = submit_post(self,'submit_edit',data)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "changed")

	def test_edit_fail(self):
		data = {
			'url':'front__',
			'title':'Front page',
			'message':'I have now changed the front page',
			'author':'harry',
		}

		response = submit_post(self,'submit_edit',data)
		self.assertEqual(response.status_code, 404)

	def test_new(self):
		data = {
			'title':'Test Page',
			'message':'This page is a test',
		}

		response = submit_post(self,'submit_new',data)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "This page is a test")

	def test_new_duplicate(self):
		data = {
			'title':'FrontPage',
			'message':'This page is a test',
		}

		response = submit_post(self,'submit_new',data)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "duplicate")

class UtilTests(TestCase):
	def setUp(self):
		return Content.objects.create(url='FrontPage',
			title = 'Front page',
			text = "Welcome to the front page",
			)

	def test_link(self):
		html = process("li:FrontPage")
		self.assertTrue("<a href=" in html)
		self.assertTrue(reverse('page', args=("FrontPage",)) in html)

	def test_diff(self):
		text1 = "Lorem ipsum dolor sit amet"
		text2 = "Lorem ipsum odor sit amet"
		d = diff(text1, text2)
		self.assertTrue("-1 +1" in d)
