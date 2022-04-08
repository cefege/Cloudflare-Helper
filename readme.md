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
1. Import `CFHelper` 
```
import CFHelper
```
2. Use `create_dns_zone` function
```
CFHelper.create_dns_zone(domain, ip, email, api_key)
```
Alternatively, 
```angular2html
python main.py --domain "" --ip "" --email "" --api-key ""
```