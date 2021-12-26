# xssping
This super short script will "ping" urls with your own custom payload. It will check to see if the payload was reflected if the response and will accordingly determine if the endpoint is potentially vulnerable or not. This is a general recon tool, not an exploitation tool; I do not reccomend to use actual XSS payloads, only strings mixed with XSS-sensitive characters like `"'</>`. Please do not rely on this script, always do manual recon too.

#How to use
First you want to prepare a file of urls with parameters. Here is how I do it with waybackurls:
1) `waybackurls target.com > urls.txt`
2) `python3 xssping.py urls.txt 'PAYLOAD"AAA' outfile.txt`

#Tips
For the first run, limit your payload to one or two sensitive characters like `"` or `<>` to avoid false negatives. My go-to payload is `VULN"AAA`. After I find the pages that reflect my payload, I go into manual recon.



