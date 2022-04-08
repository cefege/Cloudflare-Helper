import CloudFlare
from CloudFlare.exceptions import CloudFlareAPIError




def list_zones(cf):
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        print("zone_id=%s zone_name=%s" % (zone_id, zone_name))


def create_dns_zone(domain, ip, email, api_key):
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
    try:
        # Create zone with the domain name
        zone_info = cf.zones.post(data={'jump_start': False, 'name': domain})
        print(f"{domain}: CREATED.")
        # Get zone id

    except Exception as e:
        if "already exists" in str(e):
            print(f"{domain}: Already Exist.")
            zone_info = cf.zones.get(params={'name': domain})[0]
        else:
            print(f"API Exception: {str(e)}")
            exit()

    zone_id = zone_info['id']
    # Add DNS records information
    dns_records = [{'name': domain, 'type': 'A', 'content': ip, 'proxied': True},
                   {'name': 'www', 'type': 'CNAME', 'content': domain, 'proxied': True}, ]

    for dns_record in dns_records:
        try:
            r = cf.zones.dns_records.post(zone_id, data=dns_record)
            print(f"CREATED: {dns_record}")
        except CloudFlareAPIError as e:
            print(f"{dns_record} Error: {str(e)}")

    return True
