import urllib.request as request
from googleapiclient.discovery import build
import json 
import uuid
import os

URL = os.environ.get('OKTA_URL') # "https://s3.amazonaws.com/ok4ta-ip-ranges/ip_ranges.json"
TENANTS = os.environ.get('OKTA_TENANTS') # "us_cell_5,preview_cell_1"
PROJECT = os.environ.get('GCP_PROJECT')

compute = build('compute', 'v1')

def main(event, context):
    print('Event: ' + str(event))
    print('Context: ' + str(context))

    raw_ip_ranges = get_okta_ranges()
    tenant_list = TENANTS.split(",")
    print(raw_ip_ranges)
    for cell in tenant_list:
        rule_name = cell.replace('_','-')
        update_firewall(rule_name, raw_ip_ranges[cell]["ip_ranges"])

def get_okta_ranges():
    try:
        with request.urlopen(URL) as response:
            source = response.read()
            raw_ip_ranges = json.loads(source)
            return raw_ip_ranges
    except:
        print(f'An error occured when trying to retrieve {URL}')
        raise

def update_firewall(rule_name, ip_addresses):
    body = {
        'destinationRanges': ip_addresses
    }
    try:
        request = compute.firewalls().patch(project=PROJECT,firewall=f'okta-{rule_name}',body=body,requestId=uuid.uuid4())
        response = request.execute()
        return response
    except Exception as e:
        print(e)
