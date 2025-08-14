import requests
from config import TRADING_BASE, HEADERS

def main():
    r = requests.get(f"{TRADING_BASE}/v2/account", headers=HEADERS, timeout=15)
    if r.status_code == 200:
        acc = r.json()
        print("OK: Account connected")
        print("Account Number:", acc.get("account_number"))
        print("Status:", acc.get("status"))
        print("Equity:", acc.get("equity"))
        print("Buying Power:", acc.get("buying_power"))
    else:
        print("ERROR:", r.status_code, r.text)

if __name__ == "__main__":
    main()
