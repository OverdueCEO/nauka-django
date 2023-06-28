from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase
from django.urls import reverse

import sys
sys.tracebacklimit = 0


class HomeTests( SimpleTestCase):
	def test_url_exists_at_correct_location( s):
		response = s.client.get('/')
		s.assertEqual( response.status_code, 200)
	def test_url_available_by_name( s):
		response = s.client.get( reverse( 'home'))
		s.assertEqual( response.status_code, 200)
	def test_template_name_is_correct( s):
		response = s.client.get( reverse('home'))
		s.assertTemplateUsed( response, 'home.html')
	def test_template_content( s):
		response = s.client.get( reverse( 'home'))
		s.assertContains( response, '<h1>Homepage</h1>')

class AboutTests( SimpleTestCase):
	def test_url_exists_at_correct_location( s):
		response = s.client.get('/about/')
		s.assertEqual( response.status_code, 200)
	def test_url_available_by_name( s):
		response = s.client.get( reverse( 'about'))
		s.assertEqual( response.status_code, 200)
	def test_template_name_correct( s):
		response = s.client.get( reverse( 'about'))
		s.assertTemplateUsed( response, 'about.html')
	def test_template_content( s):
		response = s.client.get( reverse( 'about'))
		s.assertContains( response, '<h1>About page</h1>')
