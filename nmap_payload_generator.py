#!/usr/bin/python3

import subprocess
from time import sleep



black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
brown = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
light_gray = "\033[0;37m"
dark_gray = "\033[1;30m"
light_red = "\033[1;31m"
light_green = "\033[1;32m"
yellow = "\033[1;33m"
light_blue = "\033[1;34m"
light_purple = "\033[1;35m"
light_cyan = "\033[1;36m"
light_white = "\033[1;37m"
bold = "\033[1m"
faint = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
blink = "\033[5m"
negative = "\033[7m"
crossed = "\033[9m"
reset = "\033[0m"




def main_menu():
    subprocess.run("clear")
    print(light_green + "         MENU            " + reset)
    print()
    print(light_red + "[1] " +reset+ "- create payload")
    print(light_blue + "[2] " +reset+ "- see templates")
    print(light_red + "[3] " +reset+ "- exit")
    response = input("> ")
    if response == '1':
        create()
    elif response == '2':
        templates()
    elif response == '3':
        print("Goodbye!")
    else:
        print(light_red+"Invalid Input"+reset)
        main_menu()



def create():
    payload = "sudo nmap"
    subprocess.run("clear")
    print(light_cyan +"Scan type:"+reset)
    print(f'''
{light_green}[1] {reset}- TCP SYN port scan (Default)
{light_green}[2] {reset}- TCP connect port scan (Default without root privilege)
{light_green}[3] {reset}- UDP port scan
{light_green}[4] {reset}- TCP ACK port scan
{light_green}[5] {reset}- TCP Window port scan
{light_green}[6] {reset}- TCP Maimon port scan
{light_green}[7] {reset}- Skip''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-sS',
        '2':'-sT',
        '3':'-sU',
        '4':'-sA',
        '5':'-sW',
        '6':'-sM',
        '7':'',
    }
    try:
        payload += ' '+dictionary[response]
    except:
        print()
    
    subprocess.run("clear")
    print(light_cyan+"Host Discovery:"+reset)
    print(f'''
{light_green}[1] {reset}- No Scan. List targets only
{light_green}[2] {reset}- Disable port scanning. Host discovery only.
{light_green}[3] {reset}- Disable host discovery. Port scan only.
{light_green}[4] {reset}- TCP SYN discovery on port x. Port 80 by default
{light_green}[5] {reset}- TCP ACK discovery on port x. Port 80 by default
{light_green}[6] {reset}- UDP discovery on port x. Port 40125 by default
{light_green}[7] {reset}- ARP discovery on local network
{light_green}[8] {reset}- Never Do DNS resolution
{light_green}[9] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-sL',
        '2':'-sn',
        '3':'-Pn',
        '4':'-PS',
        '5':'-PA',
        '6':'-PU',
        '7':'-PR',
        '8':'-n',
        '9':'',
    }
    try:
        payload += ' '+dictionary[response]
    except:
        print()
    
    subprocess.run("clear")
    print(light_cyan + "Service and Version Detection:" + reset)
    print(f'''
{light_green}[1] {reset}- Detect OS 
{light_green}[2] {reset}- Detect Version of service
{light_green}[3] {reset}- Enables OS detection, version detection, script scanning, and traceroute
{light_green}[4] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-O',
        '2':'-sV',
        '3':'-A',
        '4':'',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print()

    subprocess.run("clear")
    print(light_cyan + "Scan Speed" + reset)
    print(f'''
{light_green}[1] {reset}- Paranoid - Intrusion Detection System evasion
{light_green}[2] {reset}- Sneaky - Intrusion Detection System evasion
{light_green}[3] {reset}- Polite - slows down the scan to use less bandwidth and use less target machine resources
{light_green}[4] {reset}- Normal - which is default speed
{light_green}[5] {reset}- Aggressive - speeds scans; assumes you are on a reasonably fast and reliable network
{light_green}[6] {reset}- Insane - speeds scan; assumes you are on an extraordinarily fast network
{light_green}[7] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-T0',
        '2':'-T1',
        '3':'-T2',
        '4':'-T3',
        '5':'-T4',
        '6':'-T5',
        '7':'',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print()
    

    subprocess.run("clear")
    print(light_cyan + "Scripts:" + reset)
    print(f'''
{light_green}[1] {reset}- Scan with default NSE scripts. Considered useful for discovery and safe
{light_green}[2] {reset}- Scan for vulnerabilities 
{light_green}[3] {reset}- Use only safe scripts
{light_green}[4] {reset}- Use intrusive scripts. Considered unsafe.
{light_green}[5] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-sC',
        '2':'--script=vuln',
        '3':'--script=safe',
        '4':'--script=intrusive',
        '5':'',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print()

    
    print()          
    print("Your payload is: "+light_green+ payload +" <IP address/range>" + reset)
    print("Replace <IP address/range>")
    print()








def templates():
    print("copy one of the below payloads and replace '<IP address/range>'")
    print("nmap <IP address/range>")
    print("nmap -p- -A <IP address/range>")
    print("nmap -sS -Pn -A <IP address/range>")


main_menu()
