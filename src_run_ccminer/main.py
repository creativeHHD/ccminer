import os, json, time
from progress.spinner import MoonSpinner
# banner
setting_banner = """
╔════════════════════════════════════╦════════╗
║    ████ ████ █████ █ █    ██ █████ ║  V 2.2 ║
║   ██  █ █      █   █ █   ██        ║CREATIVE║
║  ██ ███ █      █   █ █  ██   ███   ║   HD   ║
║ ██    █ █      █   █ █ ██          ╠════════╣
║██    A█C████  T█  I█V███    E█████ ║SETTING.║
╚════════════════════════════════════╩════════╝"""

running_banner = """
╔════════════════════════════════════╦════════╗
║    ████ ████ █████ █ █    ██ █████ ║  V 2.2 ║
║   ██  █ █      █     █   ██        ║CREATIVE║
║  ██ ███ █      █   █ █  ██   ███   ║   HD   ║
║ ██    █ █      █   █ █ ██          ╠════════╣
║██A    █ C███   T   I V██    E█████ ║ START  ║
╚════════════════════════════════════╩════════╝"""

# banner function
def banner(logo):
    os.system("clear")
    print(logo,"\nDevelobment by CREATIVE-HD")
    print("------------------------------------------------") 
    print("                   ACTIVE MODE\n"
        + "    ▝  ▘\n"
        + " █ ███████ █     TERMUX AUTO START \n "
        + "█ █ 2.2 █ █ CCMINER AFTER BOOT DEVICE\n"
        + "   ███████       RUNNING AUTOMATIC\n"
        + "    ██ ██                             DEC.2021")
    print("------------------------------------------------\n")


# install miner function 
def install():
    # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
    os.system("git clone https://github.com/creativeHHD/ccminer_mmv")

# run miner function
def run():
    banner(running_banner)
    with open("set-miner/miner.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        pool = loads['Pool']
        wallet = loads['Wallet']
        password = loads['Pass']
        cpu = loads['Cpu']
    if pool == "" or wallet == "":
        print("pool หรือ wallet โปรดตั้งค่าใหม่")
        time.sleep(3)
        set_miner()
    # print(pool, wallet, password, cpu)
    print("ccminer CPU3.7 for VerusHash v2.1 - 2.2 by Monkins1010 based on ccminer")
    print("Originally based on Christian Buchner and Christian H. project")
    print("\033[93mLocated at\033[00m: http://github.com/monkins1010/ccminer")
    os.system(f"cd ccminer_mmv && ./ccminer -a verus -o {pool} -u {wallet} -p {password} -t {cpu}")

def set_miner():
    banner(setting_banner)
    pool = None
    wallet = None
    password = None
    cpu = None
    try:
        pool = input("Pool[-o]: ")

        wallet = input("Wallet[-u]: ")

        password = input("Password[-p]: ")

        cpu = int(input("CPU[-t]: "))

        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        print("\nเกิดข้อผิดพลาด โปรดตรวจสอบอีกครั้ง!")
        time.sleep(2)
        set_miner()
    puts = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': password,
        'Cpu': cpu
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(puts, set, indent=4)
while True:
    os.system("clear")
with MoonSpinner("                  โปรดรอ...") as bar:
        for i in range(100):
            time.sleep(0.05)
            bar.next()
    if os.path.exists("ccminer_mmv") == False:
        install()
        break
    if os.path.exists("set-miner") == True:
        if os.path.isfile("set-miner/miner.json") == True:
            run()
            break
        else:
            set_miner()
    else:
        os.system("mkdir set-miner")        

    
    
