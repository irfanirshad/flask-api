import unittest
from unittest.mock import patch
from api.reverse_dns import reverse_dns_lookup

class ReverseDnsTestCase(unittest.TestCase):
    @patch('api.reverse_dns.dns.reversename')
    @patch('api.reverse_dns.dns.resolver')
    def test_reverse_dns_lookup(self, mock_resolver, mock_reversename):
        # Mock the resolver response
        mock_answers = mock_resolver.resolve.return_value
        mock_answers.__len__.return_value = 1
        mock_answers[0].to_text.return_value = 'example.com'
        
        ip = '192.168.1.1'
        result = reverse_dns_lookup(ip)
        
        expected_result = {'result': ['example.com']}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
