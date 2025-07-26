# nmap_scanner.py

import nmap
import sys

def nmap_scan_logic(target_ip, ports):
    nm = nmap.PortScanner()
    print(f"[*] Attempting Nmap scan on {target_ip} for ports {ports}...") # Added print
    try:
        # The scan method might take time; it's blocking
        nm.scan(target_ip, ports) 
        
        # Check if any hosts were found
        if not nm.all_hosts():
            print(f"[-] No hosts found or scanned for {target_ip} on ports {ports}. This might indicate a problem (e.g., firewall, target offline, or insufficient permissions).")
            return # Exit if no hosts found

        for host in nm.all_hosts():
            print(f"\nHost : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state()}")
            
            # Print protocol details only if there are protocols
            if nm[host].all_protocols():
                for proto in nm[host].all_protocols():
                    print(f"----------")
                    print(f"Protocol : {proto}")
                    
                    lport = list(nm[host][proto].keys())
                    lport.sort()
                    
                    if not lport:
                        print(f"    No ports found for protocol {proto}.")
                        continue

                    for port in lport:
                        port_info = nm[host][proto][port]
                        print(f"Port : {port}\tState : {port_info['state']}\tService : {port_info['name']}")
                        if 'product' in port_info and port_info['product']:
                            print(f"  Product: {port_info['product']}")
                        if 'version' in port_info and port_info['version']:
                            print(f"  Version: {port_info['version']}")
                        if 'extrainfo' in port_info and port_info['extrainfo']:
                            print(f"  Extra Info: {port_info['extrainfo']}")
            else:
                print(f"[-] No protocols/ports found for {host}.")

        print("\n[*] Nmap scan completed for all hosts processed.") # Added print

    except nmap.PortScannerError as e:
        print(f"[-] Nmap scan error: {e}")
        print("    Common Nmap errors: Nmap program not found in PATH, insufficient permissions.")
    except Exception as e:
        print(f"[-] An unexpected Python error occurred during Nmap scan: {e}")
        print("    Ensure Nmap (the command-line tool) is installed and accessible.")

# The rest of your main() function remains the same
def main():
    print("\n--- Nmap-integrated Port Scanner ---")
    print("This tool performs more comprehensive scans using the Nmap tool via its Python library.")
    print("Ensure Nmap is installed on your system.")
    print("-----------------------------------")
    target = input("Enter the target IP address or hostname: ")
    port_range = input("Enter port range (e.g., '20-100' or '80,443,22'): ")
    
    if not target or not port_range:
        print("Error: Target and port range are required.")
        return

    nmap_scan_logic(target, port_range)

if __name__ == "__main__":
    main()