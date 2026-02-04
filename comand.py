import time
import random
import os
import json


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
startlista = []
matha = []
randoma = []
spama = []
userdata = [matha, randoma, spama, startlista]

clear()
refresh()

def load_data():
    global matha, randoma, spama, userdata, startlista 
    try:
        with open("data.json", "r") as f:
            loaded = json.load(f)
            matha = loaded.get("math", [])
            randoma = loaded.get("random", [])
            spama = loaded.get("spam", [])
            startlista  = loaded.get("spam", [])
            userdata = [matha, randoma, spama, startlista]
    except FileNotFoundError:
        print("coden.data.load-data.eror-data loading error")

def save_data():
   
    all_data = {
        "math": matha,
        "random": randoma,
        "list":startlista ,
        "spam": spama
        
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
                    codsuba2 = input(f'coden.list.del.op({codsuba}).[If you agree, write yes and all elements will be deleted or write X]->')
                    clear()
                    refresh()
                    if codsuba2 == 'yes':
                        startlist = []
                    elif codsuba2 == 'x':
                       continue
                elif codsuba == 'atv2':
                   idex =input(f'coden.list.del.op({codsuba}).Name(')
                   clear()
                   refresh()
                   codsuba3 = input(f'coden.list.del.op({codsuba}).index({idex}).(Are you sure[Answer yes or x])')
                   clear()
                   refresh()
                   if codsuba3 == 'yes':
                       startlist.remove(idex)
                       save_data()
                       continue
                   elif codsuba == 'x':
                       continue
                       
            except ValueError:
                print('eror.functions.dell->Invalid Name or software error')
                time.sleep(2)
                clear()
                refresh()
                continue
        if cod == 'svd':
            # Просмотр списка
            print(f"Current list: {startlist}") # Выводим сам список для удобства
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

                # Конвертация типа данных
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
                print('---Successfully Added---')
                time.sleep(1.5)
                clear()
                refresh()

            except ValueError:
                print('---Error: Type Mismatch---')
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
                    
                    # Проверка индекса
                    if 0 <= index < len(startlist):
                        if Dattype == 'int':
                            startlist[index] = int(Name)
                        elif Dattype == 'float':
                            startlist[index] = float(Name)
                        elif Dattype == 'bool':
                            startlist[index] = Name.lower() not in ['false', '0', '']
                        else:
                            startlist[index] = str(Name)
                        
                        save_data() # Сохраняем после редактирования
                        print('---Successfully Edited---')
                    else:
                        print('---Error: Index out of range---')
                    
                    time.sleep(1.5)
                    clear()
                    refresh()
                    
            except Exception:
                print('---Error: Invalid input---')
                time.sleep(1.5)
                clear()
                refresh()

        elif cod == 'x':
            work = False
        
        else:
            clear()
            refresh()
            continue

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

commands = {
    "print": prant,
    "random": randin,
    "list": lista,
    "spam": spam,
    "math": math,
    "userdat": data
}

while True:
    load_data()
    code = input("coden.")

    if code in commands:
        clear()
        refresh()
        commands[code]()  # Вызываем функцию из словаря по ключу
    elif code == "func":
        clear()
        refresh()
        print(" coden.func.>--time,random,sleep,print,mi,func,userdat,list")
    else:
        print("such command does not exist")
        time.sleep(1.5)
        clear()
        refresh()

 


