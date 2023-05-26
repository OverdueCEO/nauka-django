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

class AboutTests( SimpleTestCase):
	def test_url_exists_at_correct_location( s):
		response = s.client.get('/about/')
		s.assertEqual( response.status_code, 200)
	def test_url_available_by_name( s):
		response = s.client.get( reverse( 'about'))
		s.assertEqual( response.status_code, 200)
