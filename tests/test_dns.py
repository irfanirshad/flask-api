import unittest
from unittest.mock import patch
from api.dns import check_dns_propagation, dns_lookup

class DNSTestCase(unittest.TestCase):
    @patch('api.dns.dns.resolver')
    def test_check_dns_propagation(self, mock_resolver):
        # Mock the resolver response
        mock_answers = mock_resolver.resolve.return_value
        mock_answers.__len__.return_value = 1
        
        url = 'example.com'
        regions = ['us', 'eu']
        result = check_dns_propagation(url, regions)
        
        expected_result = {'us': True, 'eu': True}
        self.assertEqual(result, expected_result)
    
    @patch('api.dns.dns.resolver')
    def test_dns_lookup(self, mock_resolver):
        # Mock the resolver response
        mock_answers = mock_resolver.resolve.return_value
        mock_answers.__len__.return_value = 1
        mock_answers[0].to_text.return_value = '192.168.1.1'
        
        domain = 'example.com'
        result = dns_lookup(domain)
        
        expected_result = {'result': ['192.168.1.1']}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
