import argparse

import CFHelper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script To Create New Cloudflare Zone and Configure DNS Records")
    parser.add_argument("-d", "--domain", type=str, help="Website domain name", default="venonei.xyz")
    parser.add_argument("-e", "--email", type=str, help="Account Email Used in Authentication",
                        default="dan.vermes@gmail.com")
    parser.add_argument("-k", "--api-key", type=str, help="The Global API Key",
                        default="4184170f8158cb885eab4144a9f6c20b415be")
    parser.add_argument("-a", "--ip", nargs="?", type=str, help="Website IP address", default="192.0.2.146")
    parser.add_argument("--ssl", type=str, help="Website SSL value", default="flexible")
    parser.add_argument("--delete-domain", default=False, action="store_true", help="Delete the whole website")
    parser.add_argument("--delete-dns", default="", help="Delete DNS records")
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
