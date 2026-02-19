import time
import random
import os
import json
import platform


RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"  
INVERSE = "\033[7m" 
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_BLACK = "\033[90m" 
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"
GOLD = "\033[38;5;220m"
DARK_GOLD = "\033[38;5;172m"
ORANGE = "\033[38;5;208m"
BRONZE = "\033[38;5;130m"
SILVER = "\033[38;5;250m"
NEON_GREEN = "\033[38;5;118m"
SKY_BLUE = "\033[38;5;117m"
HOT_PINK = "\033[38;5;201m"
PURPLE = "\033[38;5;135m"
AQUA = "\033[38;5;86m"
MINT = "\033[38;5;121m"
LAVENDER = "\033[38;5;183m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_GOLD = "\033[48;5;220m"


path = f'{RED}nul{RESET}'
print("...")
time.sleep(1.5)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def refresh():
    clear()
    print("==========================")
    print(f"  --- {GOLD}CODEN{RESET} {GREEN}SYSTEM{RESET}  ---     ")
    print(f"  --  Author {SKY_BLUE}DEN89023{RESET}  ---  ")
    print(f"  -- {CYAN}Directory/{RESET}{path} ---  ")
    print("==========================")
startlista = []
matha = []
randoma = []
spama = []
userdata = [matha, randoma, spama, startlista]
mods_data = []

clear()
refresh()

import platform
import os
import sys
import psutil 


GOLD = "\033[38;5;220m"    
DARK_GOLD = "\033[38;5;172m" 
INFO_LABEL = "\033[38;5;75m" 
RESET = "\033[0m"
BOLD = "\033[1m"

def get_ram_info():
    """Получает данные о памяти, если библиотека psutil доступна"""
    try:
        ram = psutil.virtual_memory()
        return f"{ram.used // (1024**2)}MB / {ram.total // (1024**2)}MB"
    except:
        return "N/A (install psutil)"

def print_fetch():
    coin = [
        f"          {GOLD}___________________________{RESET}",
        f"       {GOLD}./###########{DARK_GOLD}########{GOLD}###########\\. {RESET}",
        f"     {GOLD}/########{DARK_GOLD}######################{GOLD}########\\ {RESET}",
        f"    {GOLD}|#######{DARK_GOLD}##########################{GOLD}#######|{RESET}",
        f"   {GOLD}|######{DARK_GOLD}     ____  ____  ____  _____ _   _  {GOLD}######|{RESET}",
        f"  {GOLD}|######{DARK_GOLD}    / ___|/ __ \\|  _ \\| ____| \\ | | {GOLD}######|{RESET}",
        f"  {GOLD}|######{DARK_GOLD}   | |   | |  | | | | |  _| |  \\| | {GOLD}######|{RESET}",
        f"  {GOLD}|######{DARK_GOLD}   | |___| |__| | |_| | |___| |\\  | {GOLD}######|{RESET}",
        f"  {GOLD}|######{DARK_GOLD}    \\____|\\____/|____/|_____|_| \\_| {GOLD}######|{RESET}",
        f"   {GOLD}|######{DARK_GOLD}                            {GOLD}          ######|{RESET}",
        f"    {GOLD}\\#######{DARK_GOLD}##########################{GOLD}#######/{RESET}",
        f"     {GOLD}\\########{DARK_GOLD}######################{GOLD}########/{RESET}",
        f"       {GOLD}'\\###########{DARK_GOLD}########{GOLD}###########/'{RESET}",
        f"          {GOLD}---------------------------{RESET}"
    ]

    sys_info = [
        f"{BOLD}{GOLD}CODEN OS FETCH{RESET}",
        f"{'—'*25}",
        f"{INFO_LABEL}USER{RESET}:     {os.getlogin() if hasattr(os, 'getlogin') else ''}",
        f"{INFO_LABEL}OS{RESET}:       {platform.system()} {platform.release()}",
        f"{INFO_LABEL}KERNEL{RESET}:   {platform.machine()}",
        f"{INFO_LABEL}UPTIME{RESET}:   Stable", 
        f"{INFO_LABEL}PYTHON{RESET}:   {platform.python_version()}",
        f"{INFO_LABEL}RAM{RESET}:      {get_ram_info()}",
        f"",
        f"{GOLD}● {DARK_GOLD}● {INFO_LABEL}● {RESET}● {BOLD}●{RESET}", 
    ]

    print("\n")
    # Вывод в две колонки
    max_rows = max(len(coin), len(sys_info))
    for i in range(max_rows):
        left = coin[i] if i < len(coin) else " " * 45
        right = sys_info[i] if i < len(sys_info) else ""
        print(f"  {left}   {right}")
    
GOLD = "\033[33m"
BRIGHT_GOLD = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"


#----------DATA------------
def load_data():
    global matha, randoma, spama, userdata, startlista, mods_data
    if not os.path.exists("data.json"):
        save_data()

    try:
        with open("data.json", "r") as f:
            loaded = json.load(f)
            matha = loaded.get("math", [])
            randoma = loaded.get("random", [])
            spama = loaded.get("spam", [])
            startlista = loaded.get("list", [])
            mods_data = loaded.get("mods", []) 
            
            userdata = [matha, randoma, spama, startlista, mods_data]
    except Exception:
        print(f"{RED}coden.data.load-data.eror-data loading error{RESET}")

def save_data():
    all_data = {
        "math": matha,
        "random": randoma,
        "list": startlista,
        "spam": spama,
        "mods": mods_data 
    }
    with open("data.json", "w") as f:
        json.dump(all_data, f)
def data():
    global data_map
    data_map = {
        "math": matha,
        "random": randoma,
        "list":startlista ,
        "spam": spama,
        "all": userdata
    }
    code = input("coden.userdat.")
    if code in data_map:
        time.sleep(0.5)
        print(f"coden.userdat.{code}")
        time.sleep(0.5)
        clear()
        refresh()
        time.sleep(0.5)
        print(data_map[code])
        input("coden.userdat." ,code, ".Close.>")
        clear()
        refresh()
    else:
        print("such command does not exist")
        time.sleep(1)
        clear()
        refresh()
#--------------------------------

# functions
def path_start():
    global path
    path = input('coden.cd ')
    try:
        if os.path.exists(path) and os.path.isdir(path):
            sec = input(f'{GREEN}Successfully>cd.set>>{path}{RESET}->')
            clear()
            refresh()
        else:
            c = input(f'coden.cd.{RED}Error:Invalid.>>{path}{RESET}')
            path = 'nul'
            clear()
            refresh()
    except Exception:
        c = input(f'coden.cd.{RED}Error:Invalid.>>{path}{RESET}')
        clear()
        refresh()

def lista():
    global startlista 
    startlist = startlista 
    work = True 
    cod = input('coden.list.')
    clear()
    refresh()
    while work:
        cod = input('coden.list.')
        clear()
        refresh()
        if cod == 'del':
            try:
                codsuba = input('coden.list.del.op--(Delete all atv delete specific item atv2)->')
                clear()
                refresh()
                if codsuba == 'atv':
                    codsuba2 = input(f'coden.list.del.op({codsuba}).[If you agree, write {GREEN}yes{RESET} and all elements will be deleted or write {RED}x{RESET}]->')
                    clear()
                    refresh()
                    if codsuba2 == f'{GREEN}yes{RESET}':
                        startlist = []
                    elif codsuba2 == f'{RED}x{RESET}':
                       continue
                elif codsuba == 'atv2':
                   idex =input(f'coden.list.del.op({codsuba}).Name(')
                   clear()
                   refresh()
                   codsuba3 = input(f'coden.list.del.op({codsuba}).index({idex}).(Are you sure[Answer {GREEN}yes{RESET} or x])')
                   clear()
                   refresh()
                   if codsuba3 == f'{GREEN}yes{RESET}':
                       startlist.remove(idex)
                       save_data()
                       continue
                   elif codsuba == f'{RED}x{RESET}':
                       continue
                       
            except ValueError:
                print(f'{RED}eror.functions.dell->Invalid Name or software error{RESET}')
                time.sleep(2)
                clear()
                refresh()
                continue
        if cod == 'svd':
           
            print(f"Current list: {startlist}") 
            input('&.--Type any character to exit--.& <---> ')
            clear()
            refresh()
            continue 

        elif cod == 'add':
            try:
                val_input = input('coden.list.add.name-> ')
                clear()
                refresh()
                
                dtype = input('coden.list.add.Datatype (str/int/float/bool)-> ')
                clear()
                refresh()

                
                if dtype == 'int':
                    final_value = int(val_input)
                elif dtype == 'float':
                    final_value = float(val_input)
                elif dtype == 'bool':
                    if val_input.lower() in ['false', '0', '']:
                        final_value = False
                    else:
                        final_value = True
                else:
                    final_value = str(val_input)
                
                startlist.append(final_value)
                save_data()
                print(f'{GREEN}---Successfully Added---{RESET}')
                time.sleep(1.5)
                clear()
                refresh()

            except ValueError:
                print(f'{RED}---Error: Type Mismatch---{RESET}')
                time.sleep(1.5)
                clear()
                refresh()

        elif cod == 'edit':
            try:
                sub_cod = input('coden.list.edit.') 
                clear()
                refresh()
                
                if sub_cod == 'relist':
                    Name = input('coden.list.edit.relist.Name-->')
                    clear()
                    refresh()
                    
                    index_str = input('coden.list.edit.relist.index-->')
                    index = int(index_str) 
                    clear()
                    refresh()
                    
                    Dattype = input('coden.list.edit.relist.Datatype.')
                    clear()
                    refresh()
                    
                    
                      #The data selection function is not finalized.
                    if 0 <= index < len(startlist):
                        if Dattype == 'int':
                            startlist[index] = int(Name)
                        elif Dattype == 'float':
                            startlist[index] = float(Name)
                        elif Dattype == 'bool':
                            startlist[index] = Name.lower() not in ['false', '0', '']
                        else:
                            startlist[index] = str(Name)
                        # ----------------------------------------------------------
                        save_data() 
                        print(f'{GREEN}---Successfully Edited---{RESET}')
                    else:
                        print('---Error: Index out of range---')
                    
                    time.sleep(1.5)
                    clear()
                    refresh()
                    
            except Exception:
                print('{RED}---Error: Invalid input---{RESET}')
                time.sleep(1.5)
                clear()
                refresh()

        elif cod == 'x':
            work = False
        
        else:
            clear()
            refresh()
            continue
# MOD!!
def File():
    otv = input('coden.install_mod (yes/del) -> ')
    clear()
    refresh()
    
    if otv == f'{GREEN}yes{RESET}' or otv == 'mod':
        filepath = input('coden.path_to_file -> ')
        if os.path.exists(filepath):
            namemod = input(f'Name for log -> ')
            clear()
            refresh()
            try:
                with open(filepath, 'r', encoding='cp1251') as file:
                    cod = file.read()
                    print('---- Installing modification ---')
                    
                    
                    exec(cod, globals()) 
                    
                    if filepath not in mods_data:
                        mods_data.append(filepath)
                        save_data()
                        print(f'{GREEN}---- Mod saved to AutoRun! ---{RESET}')
                    else:
                        print(f'{GREEN}---- Mod already installed ---{RESET}')

                    time.sleep(2)
            except Exception as e:
                print(f"{RED}Error:{e}{RESET}")
                input('Press Enter...')
        else:
            print('File not found')
            time.sleep(1)

    # REMOVING THE MOD
    elif otv == 'del':
        print("Installed mods:", mods_data)
        del_path = input("Enter path to remove -> ")
        if del_path in mods_data:
            mods_data.remove(del_path)
            save_data()
            print(f"Mod removed from autorun {YELLOW}(Restart recommended){RESET}")
            input(f'{GREEN}Press Enter...{RESET}')
        else:
            print(f"{RED}Path not found in registry{RESET}")
            time.sleep(1)
            
    clear()
    refresh()
#--------------------------------------------------------------------------------

# Mathematical functions
def math():
    otv = input("coden.math.")
    clear()
    refresh()
    # Subtraction
    if otv == "minus":
        vide = int(input("coden.math.minus.vide."))
        clear()
        refresh()
        
        ipe = "coden.math.minus.vide." + str(vide) + ".mine."
        
        mine = int(input(ipe))
        clear()
        refresh()
        et = vide - mine
        
        print("coden.math.minus.vide.", vide, ".mine.", mine, "...")
        matha.append(et)
        save_data()
        print(et)
        time.sleep(5)
        clear()
        refresh()
        time.sleep(1)
    #------------------------------------------------

    # Addition
    if otv == "plus":
        vid = int(input("coden.math.plus.plasan."))
        clear()
        refresh()
        time.sleep(1)
        ip = "coden.math.plus.plasan." + str(vid) + ".pelsa."
        mne = int(input(ip))
        clear()
        refresh()
        time.sleep(1)
        et = vid + mne 
        print("coden.math.plus.plasan.", vid, ".mine.", mne, "...")
        time.sleep(2)
        clear()
        refresh()
        time.sleep(1)
        time.sleep(1)
        matha.append(et)
        save_data()
        print(et)
        time.sleep(5)
        clear()
        refresh()
        time.sleep(1)
    #--------------------------------------------------

    # Multiplication
    if otv == "multi":
        vud = int(input("coden.math.multi.vide."))
        clear()
        refresh()
        time.sleep(1)
        up = "coden.math.multi.vide." + str(vud) + ".mine."
        mud = int(input(up))
        clear()
        refresh()
        time.sleep(1)
        et = vud * mud
        matha.append(et)
        save_data()
        print("coden.math.multi.vide.", vud, ".mine.", mud, "...")
        time.sleep(2)
        clear()
        refresh()
        time.sleep(1)
        print(et)
    #-------------------------------------------------

    # Division
    if otv == "div":
        vodo = int(input("coden.math.div.vide."))
        clear()
        refresh()
        time.sleep(1)
        dp = "coden.math.div.vide." + str(vodo) + ".mine."
        modo = int(input(dp))
        clear()
        refresh()
        time.sleep(1)
        if modo == 0:
            print(f"{RED}Error:Zero division{RESET}")
            time.sleep(5)
            clear()
            refresh()
            return
        et = vodo / modo
        matha.append(et)
        save_data()
        print("coden.math.div.vide.", vodo, ".mine.", modo, "...")
        time.sleep(2)
        clear()
        refresh()
        time.sleep(1)
        print(et)
        save_data()
        time.sleep(5)
        clear()
        refresh()
    #-------------------------------------------------
        return et
# Spam word terminal
def spam():
    sp = str(input(f"coden.spam.{YELLOW}print({RESET}"))
    clear()
    refresh()
    time.sleep(1)
    sap = int(input("coden.colichistvo."))
    spama.append(sp)
    save_data()
    clear()
    refresh()
    time.sleep(1)
    jon = True 

    if type(sap) == int:
        jon = False

    while sap > 0:       
        time.sleep(0.1)
        print(sp)
        time.sleep(5)
        clear()
        refresh()
        time.sleep(1)  
        sap -= 1
#----------------------------------

# Random number
def randin():
    ram = int(input("coden.random.minimum. "))
    clear()
    refresh()
    time.sleep(1)
    ram2 = int(input("coden.random.max."))
    clear()
    refresh()
    time.sleep(1)
    conec = random.randint(ram, ram2)
    randoma.append(conec)
    save_data()
    print(f"coden.random.Generate.{conec}")
    time.sleep(3)
    clear()
    refresh()
    time.sleep(1)
#---------------------------------------------

#print
def prant():
    pr = input(f"coden.{YELLOW}print(){RESET}.")
    time.sleep(5)
    clear()
    refresh()
    time.sleep(1)
    global usercode 
    per = print(pr)
    time.sleep(5)
    clear()
    refresh()
    time.sleep(1)
    return per
#---------------------------------

# The Essential Dictionary of Command Management

commands = {
    "print": prant,
    "random": randin,
    "list": lista,
    "spam": spam,
    "math": math,
    "cd": path_start,
    "userdat": data,
    "test": File,
    "prcod":print_fetch
}

load_data() 
print("System checking mods...")
for mod_path in mods_data:
    try:
        if os.path.exists(mod_path):
            with open(mod_path, 'r', encoding='cp1251') as file: 
                globals() 
                exec(file.read(), globals()) 
                print(f"{GREEN}Mod loaded{RESET}:{PURPLE}{mod_path}{RESET}")
    except Exception as e:
        print(f"{RED}Error loading mod {mod_path}: {e}{RESET}")
time.sleep(1)

while True:
    load_data()
    code = input("coden.")

    if code in commands:
        clear()
        refresh()
        commands[code]()  
    else:
        print(f"{RED}such command does not exist{RESET}")
        time.sleep(1.5)
        clear()
        refresh()


 





