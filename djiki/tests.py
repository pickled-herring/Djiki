from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Content

# Create your tests here.
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
		response = self.client.post(reverse('submit_edit'),{
				'url':'FrontPage',
				'title':'Front page',
				'message':'I have now changed the front page',
				}, follow = True)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "changed")

	def test_edit_fail(self):
		response = self.client.post(reverse('submit_edit'),{
				'url':'front__',
				'title':'Front page',
				'message':'I have now changed the front page',
				}, follow = True)

		self.assertEqual(response.status_code, 404)

	def test_new(self):
		response = self.client.post(reverse('submit_new'),{
				'title':'Test Page',
				'message':'This page is a test',
				}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "This page is a test")

	def test_new_duplicate(self):
		response = self.client.post(reverse('submit_new'),{
				'title':'FrontPage',
				'message':'This page is a test',
				}, follow=True)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "duplicate")

	def test_date(self):
		print(timezone.now())

