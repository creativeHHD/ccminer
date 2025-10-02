import os, json, time
from progress.spinner import MoonSpinner
# banner
setting_banner = """
╔════════════════════════════════════╦════════╗
║    ████ ████ █████ █ █    ██ █████ ║  V 2.5 ║
║   ██  █ █      █   █ █   ██        ║CREATIVE║
║  ██ ███ █      █   █ █  ██   ███   ║   HD   ║
║ ██    █ █      █   █ █ ██          ╠════════╣
║██    A█C████  T█  I█V███    E█████ ║SETTING.║
╚════════════════════════════════════╩════════╝"""

running_banner = """
╔════════════════════════════════════╦════════╗
║    ████ ████ █████ █ █    ██ █████ ║  V 2.5 ║
║   ██  █ █      █     █   ██        ║CREATIVE║
║  ██ ███ █      █   █ █  ██   ███   ║   HD   ║
║ ██    █ █      █   █ █ ██          ╠════════╣
║██A    █ C███   T   I V██    E█████ ║ START  ║
╚════════════════════════════════════╩════════╝"""

# banner function
def banner(logo):
    os.system("clear")
    print(logo,"\nDevelobment AMS by CREATIVE-HD")
    print("------------------------------------------------") 
    print("                   ACTIVE MODE\n"
        + "    ▝  ▘\n"
        + " █ ███████ █     TERMUX AUTO START \n "
        + "█ █ 2.2 █ █ CCMINER AFTER BOOT DEVICE\n"
        + "   ███████       RUNNING AUTOMATIC\n"
        + "    ██ ██                             AUG.2025")
    print("------------------------------------------------\n")


    

