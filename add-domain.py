#!/usr/bin/env

import sys
import os

import pyrax
import pyrax.exceptions as exc

MVPCREATOR_IP = '166.78.237.58'
DEFAULT_TTL = 86400

def main():
    domain_name = sys.argv[1]

    pyrax.set_setting('identity_type', 'rackspace')
    creds_file = os.path.expanduser('~/.rackspace_cloud_credentials')
    pyrax.set_credential_file(creds_file)

    dns = pyrax.cloud_dns

    # Create the domain name.
    try:
        domain = dns.find(name=domain_name)
    except exc.NotFound:
        domain = dns.create(name=domain_name, emailAddress='support@mvpcreator.com', ttl=DEFAULT_TTL)

    records = [{
        'type': 'A',
        'name': domain_name,
        'data': MVPCREATOR_IP,
        'ttl': DEFAULT_TTL,
    }, {
        'type': 'CNAME',
        'name': '*.' + domain_name,
        'data': domain_name,
        'ttl': DEFAULT_TTL,
    }]

    domain.add_records(records)

if __name__ == "__main__": main()
