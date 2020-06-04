from django.test import TestCase
from django.urls import reverse
from .models import Content

# Create your tests here.
def setup():
	return Content.objects.create(text = "here lies index")

class ViewTests(TestCase):

	def test_response(self):
		setup()

		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "here lies index")

		response = self.client.get(reverse('edit'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "here lies index")
