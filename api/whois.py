import whois

def whois_query(query):
    result = whois.whois(query)
    return {'result': result}

