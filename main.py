import argparse

import CFHelper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script To Create New Cloudflare Zone and Configure DNS Records")
    parser.add_argument("-d", "--domain", type=str, help="Website domain name")
    parser.add_argument("-e", "--email", type=str, help="Account Email Used in Authentication",)

    parser.add_argument("-k", "--api-key", type=str, help="The Global API Key",)

    parser.add_argument("-a", "--ip", nargs="?", type=str, help="Website IP address", )
    parser.add_argument("--ssl", type=str, help="Website SSL value", default="flexible")
    parser.add_argument("--delete-domain", default=False, action="store_true", help="Delete the whole website")
    parser.add_argument("--delete-dns", default="", help="Delete DNS records")
    parser.add_argument("--ls", default=False, action="store_true", help="List all zones")

    args = parser.parse_args()
    assert args.ssl in ['off', 'flexible', 'full', 'strict']
    for t in args.delete_dns.split(","):
        assert t in ['', 'ALL', 'A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SOA', 'SRV', 'PTR', 'AFSDB',
                     'APL', 'CAA', 'DNSKEY', 'CDNSKEY', 'CERT', 'DCHID', 'DNAME', 'HIP',
                     'IPSECKEY', 'LOC', 'NAPTR', 'NSEC', 'RRSIG', 'RP', 'SSHFP']

    if args.delete_dns:
        CFHelper.delete_DNS_record(args.domain, args.delete_dns.split(","), args.email, args.api_key)

    if args.delete_domain:
        CFHelper.delete_domain(args.domain, args.email, args.api_key)

    if args.ip:
        CFHelper.create_dns_zone(args.domain, args.ip, args.email, args.api_key, args.ssl)

    if args.ls:
        CFHelper.list_all_zones(args.email, args.api_key)
