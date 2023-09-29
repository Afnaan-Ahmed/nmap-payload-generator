import subprocess
from time import sleep

def main_menu():
    subprocess.run("clear")
    print("         MENU            ")
    print()
    print("[1] - create payload")
    print("[2] - see templates")
    print("[3] - exit")
    response = input("> ")
    if response == '1':
        create()
    elif response == '2':
        templates()
    elif response == '3':
        print("Goodbye!")
    else:
        print("Invalid Input")
        main_menu()



def create():
    payload = "sudo nmap"
    subprocess.run("clear")
    print("Choose a scan type:")
    print('''[1] - TCP SYN port scan (Default)
[2] - TCP connect port scan (Default without root privilege)
[3] - UDP port scan
[4] - TCP ACK port scan
[5] - TCP Window port scan
[6] - TCP Maimon port scan
[7] - Skip''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print("Invalid input skipping...")
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
        print("Invalid Input")
    
    subprocess.run("clear")
    print("Host Discovery:")
    print('''[1] - No Scan. List targets only
[2] - Disable port scanning. Host discovery only.
[3] - Disable host discovery. Port scan only.
[4] - TCP SYN discovery on port x. Port 80 by default
[5] - TCP ACK discovery on port x. Port 80 by default
[6] - UDP discovery on port x. Port 40125 by default
[7] - ARP discovery on local network
[8] - Never Do DNS resolution
[9] - Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print("Invalid input skipping...")
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
        print("Invalid Input")
    
    subprocess.run("clear")
    print("Service and Version Detection:")
    print('''
[1] - Detect OS 
[2] - Detect Version of service
[3] - Enables OS detection, version detection, script scanning, and traceroute
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print("Invalid input skipping...")
        sleep(0.7)

    dictionary = {
        '1':'-O',
        '2':'-sV',
        '3':'-A',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print("Invalid Input")

    subprocess.run("clear")
    print("Scan Speed")
    print('''
[1] - Paranoid - Intrusion Detection System evasion
[2] - Sneaky - Intrusion Detection System evasion
[3] - Polite - slows down the scan to use less bandwidth and use less target machine resources
[4] - Normal - which is default speed
[5] - Aggressive - speeds scans; assumes you are on a reasonably fast and reliable network
[6] - Insane - speeds scan; assumes you are on an extraordinarily fast network
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print("Invalid input skipping...")
        sleep(0.7)

    dictionary = {
        '1':'-T0',
        '2':'-T1',
        '3':'-T2',
        '4':'-T3',
        '5':'-T4',
        '6':'-T5',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print("Invalid Input")
    

    subprocess.run("clear")
    print("Scripts:")
    print('''
[1] - Scan with default NSE scripts. Considered useful for discovery and safe
[2] - Scan for vulnerabilities 
[3] - Use only safe scripts
[4] - Use intrusive scripts. Considered unsafe.
[5] - Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print("Invalid input skipping...")
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
        print("Invalid Input")

    
    print()          
    print("Your payload is: " + payload + " <IP address/range>")
    print("Replace <IP address/range>")
    print()








def templates():
    print("copy one of the below payloads and replace '<IP address/range>'")
    print("nmap <IP address/range>")
    print("nmap -p- -A <IP address/range>")
    print("nmap -sS -Pn -A <IP address/range>")


main_menu()