import unittest
from unittest.mock import patch
from api.whois import whois_search

class WhoisTestCase(unittest.TestCase):
    @patch('api.whois.pythonwhois')
    def test_whois_search(self, mock_pythonwhois):
        # Mock the pythonwhois response
        mock_pythonwhois.get_whois.return_value = {'registrant': 'John Doe'}
        
        query = 'example.com'
        result = whois_search(query)
        
        expected_result = {'result': {'registrant': 'John Doe'}}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
