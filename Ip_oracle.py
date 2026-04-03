#The creator of this tool is Lukas✨
import requests as r
import ipaddress 
from colorama import Style, Fore
banner = rf"""{Style.BRIGHT}{Fore.CYAN}

    ________     ____                  __        
   /  _/ __ \   / __ \_________ ______/ /__      
   / // /_/ /  / / / / ___/ __ `/ ___/ / _ \     
 _/ // ____/  / /_/ / /  / /_/ / /__/ /  __/     
/___/_/       \____/_/   \__,_/\___/_/\___/      

"""


print(banner)
print("\033[1;34m============================================\033[0m")

user = input("\033[1;35m[+]Enter ip address: \033[0m")


url = f"https://ipapi.co/{user}/json/"
try:
    ipaddress.ip_address(user)
    print("")
    print("\033[1;32mValid ip address✅\033[0m".center(30))
    print("")
    response = r.get(url)
    data = response.json()
    keys = ["ip", "version", "country", "timezone", "network", "org", "latitude", "longitude", "currency_name", "region", "country_code", "country_capital", "asn"]
    for n in keys:
        
        print(f"{n.upper():15} :{data.get(n, 'N/A')}")
except ValueError:
    print("\033[1;31mWrong ip address...try again❌\033[0m".center(30))
    exit()
