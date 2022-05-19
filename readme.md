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
python main.py --domain "" --email "" --api-key "" --delete
```