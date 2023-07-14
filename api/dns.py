import dns.resolver
import subprocess
import dns.resolver

def propagation(url): # TODO: Not sure if this was what we intended.
    '''Fixed v1'''
    try:
        command = f'python /app/dnsdiag/dnsping.py -c 5 --dnssec --flags --tls -t AAAA -s 9.9.9.9 {url}'
        output = subprocess.check_output(command, shell=True).decode()
    except:
        output = "An error occurred. Please check url and try again"
    finally:
        return {'result': str(output)}




def dns_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A' )
        result = [str(answer) for answer in answers]
    except dns.resolver.NXDOMAIN:
        result = []
    
    return {'result': result}

