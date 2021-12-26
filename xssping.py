import requests
import re
import sys
import time

def select(file, payload):
    file = open(file, "r").read()
    regex = "(?<==).*?(?=&)|(?<==).*?.*"
    urls = re.sub(regex, payload, file)
    targets = []
    for line in urls.splitlines():
        if "?" and "=" in line:
            targets.append(line)    
    return targets

def run(url, payload):
    proxies = {
               'http': 'http://127.0.0.1:8080',
               'https': 'http://127.0.0.1:8080',
            }
    escaped_payload = payload.replace('"', '\\"')
    res = requests.get(url)
    if payload in res.text or escaped_payload in res.text:
        print(url, "might be vuln!")
        open(sys.argv[3], "w").write(url)
    else:
        print(url, "not vuln")
        

targets = select(sys.argv[1], sys.argv[2])
for url in targets:
    run(url, sys.argv[2])
    #time.sleep(0.5)
