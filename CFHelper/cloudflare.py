import time

import CloudFlare
from CloudFlare.exceptions import CloudFlareAPIError


def list_zones(cf):
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        print("zone_id=%s zone_name=%s" % (zone_id, zone_name))


def create_dns_zone(domain, ip, email, api_key, ssl_value, max_trial_limit=30, sleep_period=5):
    """
    Function To Create New Cloudflare Zone and Configure DNS Records
    :param domain: The website domain name
    :param ip: The website IP address
    :param email: Account Email Used in Authentication
    :param api_key: The Global API Key
    :return:
    """
    # Create Cloudflare instance
    cf = CloudFlare.CloudFlare(email=email, token=api_key)
    n_trials = 0
    while n_trials < max_trial_limit:
        try:
            # Create zone with the domain name
            zone_info = cf.zones.post(data={'jump_start': False, 'name': domain})
            print(f"{domain}: CREATED.")
            break
            # Get zone id
        except Exception as e:
            if "already exists" in str(e):
                print(f"{domain}: Already Exist.")
                zone_info = cf.zones.get(params={'name': domain})[0]
                break
            else:
                if "temporarily restricted" in str(e):
                    print(f"API Blocked: {str(e)}, Sleep for {sleep_period}s, Trial #{n_trials}")
                    n_trials += 1
                    time.sleep(sleep_period)
                else:
                    print(f"API Exception: {str(e)}")
                    exit()

    zone_id = zone_info['id']

    # Create ssl
    cf.zones.settings.ssl.patch(zone_id, data={'value': ssl_value})
    # Add DNS records information
    dns_records = [{'name': domain, 'type': 'A', 'content': ip, 'proxied': True},
                   {'name': 'www', 'type': 'CNAME', 'content': domain, 'proxied': True}, ]

    for dns_record in dns_records:
        n_trials = 0
        while n_trials < max_trial_limit:
            try:
                r = cf.zones.dns_records.post(zone_id, data=dns_record)
                print(f"DNS ZONE CREATED: {dns_record}")
                break
            except CloudFlareAPIError as e:
                if "temporarily restricted" in str(e):
                    print(f"API Blocked: {str(e)}, Sleep for {sleep_period}s, Trial #{n_trials}")
                    n_trials += 1
                    time.sleep(sleep_period)
                else:
                    print(f"{dns_record} Error: {str(e)}")
                    break
    return True


def delete_domain(domain, email, api_key):
    """
    Function to delete domain from cloudflare
    :param domain: The website domain name
    :param email: Account Email Used in Authentication
    :param api_key: The Global API Key
    """
    cf = CloudFlare.CloudFlare(email=email, token=api_key)
    zones = cf.zones.get(params={'name': domain})
    if zones:
        try:
            cf.zones.delete(zones[0]['id'])
            print(f"{domain}: Deleted Successfully.")
        except Exception as e:
            print(str(e))
    else:
        print(f"{domain} Doesn't Exist.")


def delete_DNS_record(domain, zone_types, email, api_key):
    cf = CloudFlare.CloudFlare(email=email, token=api_key)
    zone = cf.zones.get(params={'name': domain})[0]
    records = cf.zones.dns_records(zone['id'])
    for record in records:
        if 'ALL' in zone_types or record['type'] in zone_types:
            cf.zones.dns_records.delete(zone['id'], record['id'])

def list_all_zones(email, api_key):
    cf = CloudFlare.CloudFlare(email=email, token=api_key)
    for zone in cf.zones():
        pass
        # domain,ns1,ns2,ssl_type,domain_status
        print(f"{zone['name']}, {zone['name_servers'][0]},"
              f" {zone['name_servers'][1]}, "
              f"{cf.zones.settings.ssl.get(zone['id']).get('value', '')}, {zone['status']}")