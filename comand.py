import time
import random
import os
import json

usercode = "eror"
print("...")
time.sleep(1.5)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def refresh():
    clear()
    print("==========================")
    print("  --- CODEN SYSTEM   ---     ")
    print("  --  Author DEN89023  ---    ")
    print("==========================")

matha = []
randoma = []
spama = []
userdata = [matha, randoma, spama]

clear()
refresh()


def load_data():
    global matha, randoma, spama, userdata
    try:
        with open("data.json", "r") as f:
            loaded = json.load(f)
            matha = loaded.get("math", [])
            randoma = loaded.get("random", [])
            spama = loaded.get("spam", [])
            userdata = [matha, randoma, spama]
    except FileNotFoundError:
        print("eror5")


def save_data():
   
    all_data = {
        "math": matha,
        "random": randoma,
        "spam": spama
    }
    with open("data.json", "w") as f:
        json.dump(all_data, f)

def data():
    data_map = {
        "math": matha,
        "random": randoma,
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
        input("coden.userdat." ,code, ".zakrati.>")
        clear()
        refresh()
    else:
        print("such command does not exist")
        time.sleep(1)
        clear()
        refresh()

def math():
    otv = input("coden.math.")
    clear()
    refresh()
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
    
    if otv == "rasdiv":
        vodo = int(input("coden.math.rasdiv.vide."))
        clear()
        refresh()
        time.sleep(1)
        dp = "coden.math.rasdiv.vide." + str(vodo) + ".mine."
        modo = int(input(dp))
        clear()
        refresh()
        time.sleep(1)
        if modo == 0:
            print("Error: Zero division")
            time.sleep(5)
            clear()
            refresh()
            return
        et = vodo / modo
        matha.append(et)
        save_data()
        print("coden.math.rasdiv.vide.", vodo, ".mine.", modo, "...")
        time.sleep(2)
        clear()
        refresh()
        time.sleep(1)
        print(et)
        save_data()
        time.sleep(5)
        clear()
        refresh()
        
        return et

def spam():
    sp = str(input("coden.spam.print("))
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

def prant():
    pr = input("coden.print.")
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

while True:
    load_data()
    code = input("coden.")
    if code == "print":
        clear()
        refresh()
        prant()
    elif code == "random":
        clear()
        refresh()
        randin()
    elif code == "spam":
        clear()
        refresh()
        spam()
    elif code == "math":
        clear()
        refresh()
        math()
    elif code == "userdat":
        clear()
        refresh()
        data()
    elif code == "func":
        clear()
        refresh()
        print(" coden.func.time,random,sleep,print,mi,func,userdat")
    else:
        print("such command does not exist")

 

