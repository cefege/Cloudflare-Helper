# Cloudflare Helper

## Installation
### Using pip
```angular2html
pip install git+https://github.com/cefege/Cloudflare-Helper.git
```
or clone the repository
```angular2html
git clone https://github.com/cefege/Cloudflare-Helper.git
```
## Usage
- Import `CFHelper` 
```
import CFHelper
```
- Create DNS Zones
```
CFHelper.create_dns_zone(domain, ip, email, api_key, ssl_value)
```

- Remove Site from Cloudflare
```angular2html
CFHelper.delete_domain(domain, email, api_key)
```

- Remove DNS records
```angular2html
CFHelper.delete_DNS_record(domain, zone_types, email, api_key)
```
Note:
zone_type should be one or more values from the following list:
```angular2html
['', 'ALL', 'A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SOA', 'SRV', 'PTR', 'AFSDB',
                                   'APL', 'CAA', 'DNSKEY', 'CDNSKEY', 'CERT', 'DCHID', 'DNAME', 'HIP',
                                   'IPSECKEY', 'LOC', 'NAPTR', 'NSEC', 'RRSIG', 'RP', 'SSHFP']
```
For example: zone_types="A,CNAME"

- List All Zones
```angular2html
CFHelper.list_all_zones(args.email, args.api_key)
```
Alternatively, 
- Create DNS Zones
```angular2html
python main.py --domain "" --ip "" --email "" --api-key "" --ssl ""
```
Nots: Supported SSL values 
```angular2html
['off', 'flexible', 'full', 'strict']
```
- Remove Site from Cloudflare
```angular2html
python main.py --domain "" --email "" --api-key "" --delete-domain
```

- Remove DNS records
```angular2html
python main.py --domain "" --email "" --api-key "" --delete-dns ""
```

Note: --delete-dns should be one or more values from the following list:
```angular2html
['', 'ALL', 'A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SOA', 'SRV', 'PTR', 'AFSDB',
                                   'APL', 'CAA', 'DNSKEY', 'CDNSKEY', 'CERT', 'DCHID', 'DNAME', 'HIP',
                                   'IPSECKEY', 'LOC', 'NAPTR', 'NSEC', 'RRSIG', 'RP', 'SSHFP']
```
For Example: --delete-dns "A,CNAME"

- List all zones
```angular2html
python main.py --domain "" --email "" --api-key "" --ls
```