import os, json, time
import sys
import re
import pyfiglet
import colorama
from github import Github, Auth
from progress.spinner import MoonSpinner
from colorama import init, Fore, Style
init(autoreset=True)
# banner
setting_banner = """
╔════════════════════════════════════╦════════╗
║    ████ ████ █████ █ █    ██ █████ ║  V 3.2 ║
║   ██  █ █      █   █ █   ██        ║CREATIVE║
║  ██ ███ █  GITHUB SUPPORT    ███   ║   HD   ║
║ ██    █ █      █   █ █ ██          ╠════════╣
║██    A█C████  T█  I█V███    E█████ ║SETTING.║
╚════════════════════════════════════╩════════╝"""

running_banner = """
╔════════════════════════════════════╦════════╗
║    ████ ████ █████ █ █    ██ █████ ║  V 3.2 ║
║   ██  █ █      █     █   ██        ║CREATIVE║
║  ██ ███ █  GITHUB SUPPORT    ███   ║   HD   ║
║ ██    █ █      █   █ █ ██          ╠════════╣
║██A    █ C███   T   I V██    E█████ ║ START  ║
╚════════════════════════════════════╩════════╝"""

# banner function
def banner(logo):
    os.system("clear")
    print(logo,"         \nDevelop by CREATIVE-HD")
    print("------------------------------------------------") 
    print("                   ACTIVE MODE\n"
        + "    ▝  ▘         GitHub Support\n"
        + " █ ███████ █     TERMUX AUTO START \n "
        + "█ █ 3.2 █ █ CCMINER AFTER BOOT DEVICE\n"
        + "   ███████       RUNNING AUTOMATIC\n"
        + "    ██ ██                             AUG.2025")
    print("------------------------------------------------\n")


# install miner function 
def install():
    # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
    os.system("git clone https://github.com/creativeHHD/ccminer_mmv")

# run miner function
def run():
    banner(running_banner) # สมมติว่าฟังก์ชันนี้มีอยู่แล้ว
    with open("set-miner/miner.json", encoding="utf-8") as set_file:
        loads = json.load(set_file)
        namepro = loads['namepro']
        droom = loads['droom']
        rig_name = loads['Rname']

    if not all([namepro, droom, rig_name]):
        print("ระบุ NameProject, Room หรือ Rig Name ให้ครบถ้วน โปรดตั้งค่าใหม่")
        time.sleep(3)
        set_miner()
        return

    access_token = os.environ.get("GITHUB_ACCESS_TOKEN")
    if not access_token:
        print(f"{Fore.RED}Error: GITHUB_ACCESS_TOKEN not found. Set the environment variable.")
        return
    try:
        g = Github(auth=Auth.Token(access_token))
        repo_name = f"creativeHHD/{namepro}"
        repo = g.get_repo(repo_name)
        file_path = f"{droom}.txt"
        
        file_content_obj = repo.get_contents(file_path)
        file_content = file_content_obj.decoded_content.decode('utf-8')

        lines = file_content.strip().split('\n')
        
        found_line = None
        for line in lines:
            if rig_name in line:
                found_line = line
                break
            
        if found_line:
            os.system("clear")
            print(f"Content for rig '{rig_name}':")
            print(found_line)
            
            try:
                values = [v.strip() for v in found_line.split('|')]
                status = values[0]
                pool = values[1]
                wallet = values[2]
                extracted_rig_name = values[3] # เปลี่ยนชื่อตัวแปรเพื่อความชัดเจน
                password = values[4]
                cpu = values[5] if len(values) > 5 else "N/A"

                os.system(f"cd ccminer_mmv && ./ccminer -a verus -o {pool} -u {wallet}.{extracted_rig_name} -p {password} -t {cpu}")
                
                #print("ccminer CPU3.7 for VerusHash v2.1 - 2.2 by Monkins1010 based on ccminer")
                #print("Originally based on Christian Buchner and Christian H. project")
                #print("\033[93mLocated at\033[00m: http://github.com/monkins1010/ccminer")
                #print(f"Pool: {pool}, Wallet: {wallet}, Password: {password}, Rig Name: {extracted_rig_name}, CPU: {cpu}")
                
            except IndexError:
                print(f"\n{Fore.RED}{Style.BRIGHT}⚠️ Error: The row does not have enough columns to parse.")
        else:
            print(f"\n{Fore.RED}{Style.BRIGHT}⚠️ Rig name '{rig_name}' not found in the file.")
            
    except Exception as e:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ An error occurred: {e}")

def set_miner():
    banner(setting_banner) # สมมติว่าฟังก์ชันนี้มีอยู่แล้ว
    while True:
        try:
            namepro = input("Enter name project : ")
            droom = input("Enter room project : ")
            Rname = input("Enter Worker Name : ")
            
            if not all([namepro, droom, Rname]):
                print(f"\n{Fore.RED}เกิดข้อผิดพลาด: โปรดระบุข้อมูลให้ครบถ้วน!")
                time.sleep(2)
                continue
            
            puts = {
                'namepro': namepro,
                'droom': droom,
                'Rname': Rname
            }
            with open("set-miner/miner.json", "w") as set_file:
                json.dump(puts, set_file, indent=4)
            break
        except Exception as e:
            print(f"\n{Fore.RED}เกิดข้อผิดพลาด: {e}")
            time.sleep(2)

# โค้ดหลัก
if __name__ == "__main__":
    while True:
        os.system("clear")
        with MoonSpinner(text="                 โปรดรอ...", color="yellow") as bar:
            for _ in range(100):
                time.sleep(0.05)
                bar.next()

        if not os.path.exists("ccminer_mmv"):
            # ควรจะมีฟังก์ชัน install() ที่ดาวน์โหลดและติดตั้ง ccminer
            print("ccminer_mmv not found. Running installation...")
            install()
            break
        
        if os.path.exists("set-miner"):
            if os.path.isfile("set-miner/miner.json"):
                run()
                break
            else:
                set_miner()
        else:
            os.system("mkdir set-miner")
            set_miner()    
    
