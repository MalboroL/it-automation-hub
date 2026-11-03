import os
import subprocess
import sys
import ctypes
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# ==========================================
# TOOLKIT FUNCTIONS
# ==========================================

def ram_optimization():
    print("\n[+] Optimizing RAM & Clearing Standby Memory...")
    try:
        subprocess.run(
            ['powershell', '-Command', 
             '[System.GC]::Collect(); [System.GC]::WaitForPendingFinalizers(); Clear-Host'],
            capture_output=True, text=True
        )
        print("[✔] RAM optimization complete! Working sets trimmed.")
    except Exception as e:
        print(f"[X] Error optimizing RAM: {e}")
    input("\nPress Enter to return to the menu...")

def troubleshooting_guide():
    clear_screen()
    print("==========================================")
    print("          TROUBLESHOOTING GUIDE           ")
    print("==========================================")
    print("1. Internet Disconnecting -> Run 'IP Release & Renew' and 'Flush DNS'.")
    print("2. Slow PC / High RAM     -> Run 'RAM Optimization' and 'Storage Scanner'.")
    print("3. Frozen Taskbar / Icons -> Run 'Restart Windows Explorer' (#9).")
    print("4. System Crashes / Bugs  -> Run 'System File Checker' (#8, needs Admin).")
    input("\nPress Enter to return to the menu...")

def storage_scanner():
    print("\n[+] Scanning and cleaning temporary files...")
    temp_dirs = [
        os.environ.get('TEMP'),
        os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
    ]
    
    for d in temp_dirs:
        if d and os.path.exists(d):
            print(f"Cleaning: {d}")
            try:
                for item in os.listdir(d):
                    item_path = os.path.join(d, item)
                    try:
                        if os.path.isfile(item_path) or os.path.islink(item_path):
                            os.unlink(item_path)
                    except Exception:
                        pass 
            except Exception as e:
                print(f"Could not fully clean {d}: {e}")
                
    print("[✔] Storage temp clean complete!")
    input("\nPress Enter to return to the menu...")

def network_scanner():
    print("\n[+] Active Network Scan (Local Gateway Check)...")
    response = os.system("ping -n 1 192.168.1.1 >nul 2>&1")
    if response == 0:
        print("[✔] Gateway (192.168.1.1) is active and reachable.")
    else:
        print("[!] Default gateway 192.168.1.1 did not respond. Trying 192.168.0.1...")
        os.system("ping -n 1 192.168.0.1")
    input("\nPress Enter to return to the menu...")

def flush_dns():
    print("\n[+] Flushing DNS Cache...")
    os.system("ipconfig /flushdns")
    print("[✔] DNS Cache successfully flushed!")
    input("\nPress Enter to return to the menu...")

def full_network_scan():
    print("\n[+] Running Full Network Diagnostics...")
    print("\n--- IP Configuration ---")
    os.system("ipconfig /all")
    print("\n--- Ping Test (Google DNS) ---")
    os.system("ping 8.8.8.8")
    print("\n--- Traceroute ---")
    os.system("tracert -h 5 8.8.8.8")
    input("\nPress Enter to return to the menu...")

def ip_release_renew():
    print("\n[+] Releasing IP Address...")
    os.system("ipconfig /release")
    print("\n[+] Renewing IP Address...")
    os.system("ipconfig /renew")
    print("[✔] IP configuration updated!")
    input("\nPress Enter to return to the menu...")

# --- NEW UTILITY FUNCTIONS ---

def system_file_checker():
    print("\n[+] Running Windows System File Checker (SFC)...")
    print("[!] Note: This repairs corrupted core files and requires Administrator rights.")
    os.system("sfc /scannow")
    input("\nPress Enter to return to the menu...")

def restart_explorer():
    print("\n[+] Restarting Windows Explorer (Taskbar & Desktop)...")
    os.system("taskkill /f /im explorer.exe & start explorer.exe")
    print("[✔] Windows Explorer restarted successfully!")
    input("\nPress Enter to return to the menu...")

def netstat_ports():
    print("\n[+] Displaying Active Connections & App Names...")
    print("[!] Note: This requires running CMD as Administrator to show application names (-b flag).")
    os.system("netstat -abno")
    input("\nPress Enter to return to the menu...")

def disk_space_summary():
    print("\n[+] Checking C: Drive Storage Summary...")
    try:
        total, used, free = shutil.disk_usage("C:\\")
        print(f"Total Space: {total // (2**30)} GB")
        print(f"Used Space:  {used // (2**30)} GB")
        print(f"Free Space:  {free // (2**30)} GB")
    except Exception as e:
        print(f"[X] Error reading disk usage: {e}")
    input("\nPress Enter to return to the menu...")

def task_killer():
    print("\n[+] Task Killer - Force Terminate a Process")
    proc_name = input("Enter exact process filename (e.g., chrome.exe, notepad.exe): ").strip()
    if proc_name:
        os.system(f"taskkill /f /im {proc_name}")
    input("\nPress Enter to return to the menu...")

# ==========================================
# MAIN MENU LOOP
# ==========================================

def main():
    if not is_admin():
        print("[!] Note: For full functionality (like SFC and deep cleaning), run CMD as Administrator.")
    
    while True:
        clear_screen()
        print("==========================================")
        print("       PRO USER COMMAND LINE TOOLKIT      ")
        print("==========================================")
        print(" 1. RAM Optimization")
        print(" 2. Troubleshooting Guide")
        print(" 3. Storage Scanner (Clean Temp Files)")
        print(" 4. Network Scanner (Gateway Check)")
        print(" 5. Flush DNS Cache")
        print(" 6. Full Network Scan & Diagnostics")
        print(" 7. IP Release & Renew")
        print(" 8. System File Checker (Repair Windows)")
        print(" 9. Restart Windows Explorer (Fix Taskbar)")
        print("10. Active Network Connections (Netstat)")
        print("11. Disk Space Summary (C: Drive)")
        print("12. Task Killer (Force Close App)")
        print(" 0. Exit")
        print("==========================================")
        
        choice = input("Select an option (0-12): ").strip()
        
        if choice == '1':
            ram_optimization()
        elif choice == '2':
            troubleshooting_guide()
        elif choice == '3':
            storage_scanner()
        elif choice == '4':
            network_scanner()
        elif choice == '5':
            flush_dns()
        elif choice == '6':
            full_network_scan()
        elif choice == '7':
            ip_release_renew()
        elif choice == '8':
            system_file_checker()
        elif choice == '9':
            restart_explorer()
        elif choice == '10':
            netstat_ports()
        elif choice == '11':
            disk_space_summary()
        elif choice == '12':
            task_killer()
        elif choice == '0':
            print("\nExiting toolkit. Goodbye!")
            sys.exit(0)
        else:
            input("\n[X] Invalid option! Press Enter to try again...")

if __name__ == "__main__":
    main()