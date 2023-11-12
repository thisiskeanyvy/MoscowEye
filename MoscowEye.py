import os, maxminddb, json, time
from colorama import init, Fore, Back, Style

version = "1.0"

def clear():
   if os.name == 'nt':
       _ = os.system('cls')
   else:
       print("\x1b[8;39;89t")
       _ = os.system('clear')

def quit():
    print("\n  Sortie du programme...")
    exit()

def graphics():
    clear()
    loading = '  Lancement de MoscowEye...'
    print("\n" + Fore.YELLOW)
    for i in range(len(loading)):
        print(loading[i], sep='', end='', flush=True); time.sleep(0.2)
    print(Fore.RESET)
    clear()
    print(Fore.GREEN + """
       180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
        |     |     |     |     |     |     |     |     |     |     |     |     |
    90N-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90N
        |           . _..::__:  ,-"-"._        |]       ,     _,.__             |
        |   _.___ _ _<_>`!(._`.`-.    /         _._     `_ ,_/  '  '-._.---.-.__|
        |>.{     " " `-==,',._\{  \  / {)      / _ ">_,-' `                /-/ _|
    60N-+  \_.:--.       `._ )`^-. "'       , [_/"""+Fore.RESET+Back.RED+"""2"""+Fore.GREEN+Back.RESET+"""(          """+Fore.RESET+Back.RED+"""3"""+Fore.GREEN+Back.RESET+"""           __,/-' +-60N
        | '"'     \         "    _L        | """+Fore.RESET+Back.RED+"""1"""+Fore.GREEN+Back.RESET+""" -_,--'              )     /. (|  |
        |          |    """+Fore.RESET+Back.RED+"""11"""+Fore.GREEN+Back.RESET+"""     ,'          _)_.\\._<> {}              _,'  """+Fore.RESET+Back.RED+"""4"""+Fore.GREEN+Back.RESET+"""/  ' |
        |          `.         /           ["""+Fore.RESET+Back.RED+"""10"""+Fore.GREEN+Back.RESET+"""_/_'"""+Fore.RESET+Back.RED+"""9"""+Fore.GREEN+Back.RESET+"""` `"(                <'}  """+Fore.RESET+Back.RED+"""5"""+Fore.GREEN+Back.RESET+""")  |
    30N-+           \\    .-. )            /-- - `-'"..' `:._     """+Fore.RESET+Back.RED+"""6"""+Fore.GREEN+Back.RESET+"""   _)  '      +-30N
        |    `        \  (  `(           /         `:\  > \  ,-^.  /' '         |
        |              `._,   ""         |           \`'   \|   ?_)  {\         |
        |                 `=.---.        `._._       ,'     "`  |' ,- '.        |
    000-+                   |    `-._         |     /          `:`<_|h--._      +-000
        |                   (   """+Fore.RESET+Back.RED+"""12"""+Fore.GREEN+Back.RESET+"""   >        .     | ,          `=.__.`-'\     |
        |                    `.     /         |  """+Fore.RESET+Back.RED+"""8"""+Fore.GREEN+Back.RESET+"""  |{|              ,-.,\     .|
        |                     |   ,'           \   / `'            ," """+Fore.RESET+Back.RED+"""7"""+Fore.GREEN+Back.RESET+"""   \     |
    30S-+                     |  /              |_'                |  __  /     +-30S
        |                     | |                                  '-'  `-'   \.|
        |                     |/                                         "    / |
        |                     \.                                             '  |
    60S-+                                                                       +-60S
        |                      ,/            ______._.--._ _..---.---------._   |
        |     ,-----"-..?----_/ )      __,-'"             "                  (  |
        |-.._(                  `-----'                                       `-|
    90S-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90S""" +
    f"""
        |  {Fore.RESET}{Back.MAGENTA}- MoscowEye v{version} -{Back.YELLOW} by Keany Vy KHUN{Back.RED} -/python3 MoscowEye.py --help{Back.RESET}{Fore.GREEN}    |
        |     |     |     |     |     |     |     |     |     |     |     |     |
       180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
        +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    """ + Fore.RESET)

"""def get_ip_info(code):
    if code == "1":
        ip = ""
    elif code == "2":
        ip = ""
    elif code == "3":
        ip = ""
    else:
        quit()
    with maxminddb.open_database('GeoOpen-Country-ASN.mmdb') as reader:
        ip_info = reader.get(ip)
        pays = ip_info['country']['iso_code']
        org = ip_info['country']['AutonomousSystemOrganization']
        if "none" in pays or "not routed" in org.lower():
            print("ok")
        print(pays+":"+org)
        print(ip_info)"""

if __name__ == "__main__":
    graphics()
    print(f"        {Back.BLUE}Choisissez un numéro de pays disponible (ex: 1,2,3 ...)" + Back.RESET + "\n")
    code = input("        - Localisation: ")
    if code == "/quit":
        print("\n  Sortie du programme...")
        exit()
    #get_ip_info(code)