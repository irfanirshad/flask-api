import dns.resolver, dns.reversename

def reverse_dns_lookup(ip):
    try:
        reverse_name = dns.reversename.from_address(ip)
        answers = dns.resolver.resolve(reverse_name, 'PTR')
        return [str(answer) for answer in answers]
    except dns.resolver.NXDOMAIN:
        return []
