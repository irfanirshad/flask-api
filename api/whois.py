import pythonwhois


def whois(query):
    result = pythonwhois.get_whois(query)
    return { 'result' : result }