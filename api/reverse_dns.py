import dns.reversename, dns.resolver

def reverse_dns(ip):
    try:
        reverse_name = dns.reversename.from_address(ip)
        answers = dns.resolver.resolve(reverse_name, 'PTR')
        result = [str(answer) for answer in answers]
    except dns.resolver.NXDOMAIN:
        result = []

    return { 'result': result }

