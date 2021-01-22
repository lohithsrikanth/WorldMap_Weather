import unittest
from country_codes import get_country_code

class TestCountryCodes(unittest.TestCase):
	"""Class to test the get_country_code function"""
	def test_get_country_code(self):
		country = 'India'
		self.assertEqual('in', get_country_code(country))
		
	def test_get_no_country_code(self):
		country = 'Auckland'
		self.assertEqual(None, get_country_code(country)) 
				
unittest.main()
