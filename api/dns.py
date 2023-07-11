import dns.resolver

import dns.resolver

def check_dns_propogation(url, regions): # TODO: dnspython not working ..need another library to fix this
    '''Needs to be fixed...'''
    results = {}

    resolver = dns.resolver.Resolver()

    for region in regions:
        try:
            resolver.nameservers = [dns.resolver.zone_for_name(region).to_text()]
            answers = resolver.resolve(url, 'A')
            results[region] = len(answers) > 0
        except dns.resolver.NXDOMAIN:
            results[region] = False

    return results



def dns_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A' )
        result = [str(answer) for answer in answers]
    except dns.resolver.NXDOMAIN:
        result = []
    
    return {'result': result}

