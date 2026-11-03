import os
import subprocess
import sys
import shutil

def clear_screen():
    os.system('clear')

def is_admin():
    return os.geteuid() == 0

# ==========================================
# TOOLKIT FUNCTIONS (macOS VERSION)
# ==========================================

def ram_optimization():
    print("\n[+] Optimizing RAM & Purging Inactive Memory...")
    print("[!] Note: Purging memory on macOS requires administrator (sudo) privileges.")
    try:
        # macOS built-in memory purge command
        res = os.system("sudo purge")
        if res == 0:
            print("[✔] Inactive memory successfully purged!")
        else:
            print("[!] Memory purge failed. Try launching the script with 'sudo python3 toolkit_mac.py'")
    except Exception as e:
        print(f"[X] Error purging RAM: {e}")
    input("\nPress Enter to return to the menu...")

def troubleshooting_guide():
    clear_screen()
    print("==========================================")
    print("       macOS TROUBLESHOOTING GUIDE        ")
    print("==========================================")
    print("1. Internet Disconnecting -> Run 'Flush DNS' and 'Renew DHCP Lease'.")
    print("2. Unresponsive UI        -> Run 'Restart Finder / Dock'.")
    print("3. App Freezes            -> Use 'Task Killer (pkill)'.")
    print("4. Check Active Ports     -> Run 'Active Network Connections' (lsof/netstat).")
    input("\nPress Enter to return to the menu...")

def storage_scanner():
    print("\n[+] Cleaning User Caches & Temp Files...")
    user_cache = os.path.expanduser('~/Library/Caches')
    print(f"Targeting: {user_cache}")
    
    try:
        if os.path.exists(user_cache):
            count = 0
            for item in os.listdir(user_cache):
                item_path = os.path.join(user_cache, item)
                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                        count += 1
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                        count += 1
                except Exception:
                    pass
            print(f"[✔] Removed {count} cache folders/files!")
    except Exception as e:
        print(f"[X] Error cleaning cache: {e}")
    input("\nPress Enter to return to the menu...")

def network_scanner():
    print("\n[+] Active Network Scan (Gateway Check)...")
    response = os.system("ping -c 1 192.168.1.1 > /dev/null 2>&1")
    if response == 0:
        print("[✔] Gateway (192.168.1.1) is active and reachable.")
    else:
        print("[!] Gateway 192.168.1.1 did not respond. Trying 192.168.0.1...")
        os.system("ping -c 1 192.168.0.1")
    input("\nPress Enter to return to the menu...")

def flush_dns():
    print("\n[+] Flushing mDNSResponder (DNS Cache)...")
    os.system("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder")
    print("[✔] DNS Cache successfully flushed!")
    input("\nPress Enter to return to the menu...")

def full_network_scan():
    print("\n[+] Running Full macOS Network Diagnostics...")
    print("\n--- Network Interface Status ---")
    os.system("ifconfig en0")
    print("\n--- Ping Test (Google DNS) ---")
    os.system("ping -c 4 8.8.8.8")
    print("\n--- Traceroute ---")
    os.system("traceroute -m 5 8.8.8.8")
    input("\nPress Enter to return to the menu...")

def ip_release_renew():
    print("\n[+] Renewing DHCP Lease on Wi-Fi (en0)...")
    os.system("sudo ipconfig set en0 DHCP")
    print("[✔] DHCP Lease renewed!")
    input("\nPress Enter to return to the menu...")

def restart_finder():
    print("\n[+] Restarting Finder & Dock...")
    os.system("killall Finder")
    os.system("killall Dock")
    print("[✔] macOS Finder and Dock restarted!")
    input("\nPress Enter to return to the menu...")

def netstat_ports():
    print("\n[+] Displaying Active ESTABLISHED Network Connections...")
    os.system("netstat -anv | grep ESTABLISHED")
    input("\nPress Enter to return to the menu...")

def disk_space_summary():
    print("\n[+] Storage Usage Summary (Macintosh HD)...")
    os.system("df -h /")
    input("\nPress Enter to return to the menu...")

def task_killer():
    print("\n[+] Task Killer - Force Terminate a Process")
    proc_name = input("Enter app name (e.g., Safari, Chrome, Finder): ").strip()
    if proc_name:
        os.system(f"killall -9 '{proc_name}'")
    input("\nPress Enter to return to the menu...")

# ==========================================
# MAIN MENU LOOP
# ==========================================

def main():
    if not is_admin():
        print("[!] Tip: For system actions like RAM Purging and DNS Flushing, run terminal using 'sudo python3 toolkit_mac.py'.")
    
    while True:
        clear_screen()
        print("==========================================")
        print("    macOS PRO USER COMMAND LINE TOOLKIT   ")
        print("==========================================")
        print(" 1. RAM Optimization (Purge Inactive RAM)")
        print(" 2. Troubleshooting Guide")
        print(" 3. Storage Scanner (Clean Cache)")
        print(" 4. Network Scanner (Gateway Check)")
        print(" 5. Flush DNS Cache")
        print(" 6. Full Network Scan & Diagnostics")
        print(" 7. Renew DHCP Lease (IP Renew)")
        print(" 8. Restart Finder & Dock")
        print(" 9. Active Network Connections (Netstat)")
        print("10. Disk Space Summary")
        print("11. Task Killer (killall -9)")
        print(" 0. Exit")
        print("==========================================")
        
        choice = input("Select an option (0-11): ").strip()
        
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
            restart_finder()
        elif choice == '9':
            netstat_ports()
        elif choice == '10':
            disk_space_summary()
        elif choice == '11':
            task_killer()
        elif choice == '0':
            print("\nExiting toolkit. Goodbye!")
            sys.exit(0)
        else:
            input("\n[X] Invalid option! Press Enter to try again...")

if __name__ == "__main__":
    main()