import pythonwhois

def get_whois(query):
    try:
        result = pythonwhois.get_whois(query)
        return result
    except pythonwhois.exceptions.WhoisLookupError:
        return {}
