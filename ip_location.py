import requests
from requests import get

def ipLocation():
    ip = get('https://api.ipify.org').text
    
    detail = ""

    response = requests.post("http://ip-api.com/batch", json=[
      {"query": ip}
    ]).json()

    for ip_info in response:
        for loc in ip_info.items():
            detail = detail + str(loc) + "\n"
            #print(str(loc))
        #detail = detail + "\n"
        #print("\n")


    return detail