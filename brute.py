import time
import os
try:
    import urllib.request
except:
    print("Looks like you don't have the URLLib Library, Installing...")
    os.system("pip install urllib")
    os.system("pip3 install urllib")
    print("")
    print("We have installed URLLib, Restart.")
try:
    from colorama import *
except:
    print("Looks like you don't have the Colorama Library, Installing...")
    os.system("pip install colorama")
    os.system("pip3 install colorama")
    print("")
    print("We have installed Colorama, Restart.")
init()

f = open("words.txt", "r").read().splitlines()
f2 = open("domains.txt", "r").read().splitlines()
hit = open("working.txt", "w")

ascii = """\
 █     █░▓█████  ▄▄▄▄          ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████ 
▓█░ █ ░█░▓█   ▀ ▓█████▄       ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀ 
▒█░ █ ░█ ▒███   ▒██▒ ▄██      ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███   
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀        ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓      ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒      ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░       ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░
  ░   ░     ░    ░    ░        ░    ░   ░░   ░  ░░░ ░ ░   ░         ░   
    ░       ░  ░ ░             ░         ░        ░                 ░  ░
                      ░             ░                                   """

print(Fore.GREEN + ascii)
print("")
print("")
print(Fore.RED + "WARNING! The vulnerability script will utilise the nmap command not library")
print(Fore.CYAN + "Starting..." + Fore.RESET)
print("")
print("")
time.sleep(3)


for line in f:
    for lines in f2:
        try:
            combo = line + "." + lines
            response = urllib.request.urlopen("https://" + combo).getcode()
            if(response == 200):
                print(Fore.GREEN + "[+] " + Fore.CYAN + combo + " Is Online! Writing to file")
                hit.write(combo + "\n")
        except:
            pass
print(Fore.MAGENTA + "Finished checking, Writing to file.")
hit.close()
a = input("Would you like to scan vulnerabilities (Y/N): ")
if(a.lower() == "y"):
    hits = open("working.txt", "r").read().splitlines()
    for line in hits:
        print("Starting" + Fore.YELLOW)
        try:
            os.system("nmap --script vuln " + line)
        except:
            print("Something went wrong, Continuing...")
            pass
elif(a.lower() == "n"):
    print("Exiting in 3 seconds...")
    time.sleep(3)
    exit(0)
