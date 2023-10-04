import os, json, time
from progress.spinner import MoonSpinner

# banner
edit_banner = """
╔════════════════════════════════════╦════════╗
║    ████ ████ █████ █ █    ██ █████ ║   V.1  ║
║   ██  █ █      █   █ █   ██        ║CREATIVE║
║  ██ ███ █      █   █ █  ██   ███   ║   HD   ║
║ ██    █ █      █   █ █ ██          ╠════════╣
║██   A █C████ T █  I█V███   E █████ ║  EDIT  ║
╚════════════════════════════════════╩════════╝"""

# banner function
def banner(logo):
    os.system("clear")
    print(logo,"\nDevelobment by CREATIVE-HD")
    print("-------------------------------------------------") 
    print("                   EDIT MODE\n"
        + ""
        + "            โหมดแก้ไข TERMUX AUTO START \n"
        + "            CCMINER AFTER BOOT DEVICE\n"
        + "                RUNING AUTOMATIC\n"
        + "                                         DEC.2021")
    print("--------------------------------------------------\n")

# setting function
def set_miner():
    banner(edit_banner)
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

# check path & main process
os.system("clear")
with MoonSpinner("                  โปรดรอ...") as bar:
        for i in range(100):
            time.sleep(0.05)
            bar.next()
if os.path.exists("set-miner") == True:
    set_miner()
else:
    os.system("mkdir set-miner")
    
