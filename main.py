from flask import Flask, jsonify, request
from api.dns import check_dns_propogation, dns_lookup
from api.reverse_dns import reverse_dns
from api.whois import whois_query
from dns import resolver, reversename
import subprocess
import time

app = Flask(__name__)

# @app.route('/dns/propogation', methods = ['POST'])
# def dns_propogation():
#     data = request.json
#     url = data.get('url')
#     regions = data.get('regions')

#     if not url or not regions:
#         return jsonify({"error": 'Invalid request'}), 400
    
#     result = check_dns_propogation(url, regions)
#     return jsonify(result)

@app.route('/dns-propagation', methods=['POST'])
def dns_propagation():
    url = request.json['url']  # Assuming the URL is provided in the JSON payload

    try:
        command = f'/app/venv/bin/dnsping.py -c 5 --dnssec --flags --tls -t AAAA -s 9.9.9.9 {url}'
        output = subprocess.check_output(command, shell=True).decode()

        return output

    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/dns/lookup', methods=['POST'])
def dns_lookup_endpoint():
    data = request.json
    domain = data.get('domain')

    if not domain:
        return jsonify({"error": 'Invalid request'}), 400
    
    result = dns_lookup(domain)
    return jsonify(result)


@app.route('/whois/search', methods=['POST'])
def whois_search_endpoint():
    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({ "error": 'Invalid request' }), 400
    
    result = whois_query(query)
    return jsonify(result)


@app.route('/reverse-dns/lookup', methods=['POST'])
def reverse_dns_lookup_endpoint():
    data = request.json
    ip = data.get('ip')

    if not ip:
        return jsonify({ "error": 'Invalid request' }), 400
    
    result = reverse_dns(ip)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)
