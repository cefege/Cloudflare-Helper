import argparse

import CFHelper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script To Create New Cloudflare Zone and Configure DNS Records")
    parser.add_argument("-d", "--domain", type=str, help="Website domain name")
    parser.add_argument("-e", "--email", type=str, help="Account Email Used in Authentication")
    parser.add_argument("-k", "--api-key", type=str, help="The Global API Key")
    parser.add_argument("-a", "--ip", nargs="?", type=str, help="Website IP address")
    parser.add_argument("--delete", default=False, action="store_true", help="Delete the whole website")
    args = parser.parse_args()

    if args.delete:
        CFHelper.delete_domain(args.domain, args.email, args.api_key)

    if args.ip:
        CFHelper.create_dns_zone(args.domain, args.ip, args.email, args.api_key)
