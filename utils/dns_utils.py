import dns.resolver

def resolve_dns(url, record_type='A', region=None):
    try:
        answers = dns.resolver.resolve(url, record_type, region=region)
        return [str(answer) for answer in answers]
    except dns.resolver.NXDOMAIN:
        return []
