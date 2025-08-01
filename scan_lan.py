import ipaddress
import socket
import psutil
import platform
import subprocess
import threading
import re
import time

alive_hosts = []

def get_active_subnet():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                ip = addr.address
                netmask = addr.netmask
                if ip and netmask:
                    interface_network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                    print(f"🌐 Interfață activă: {interface} ({ip}/{netmask})")
                    return interface_network
    raise RuntimeError("Nu s-a putut detecta o interfață activă cu IP valid.")

def ping(ip):
    system = platform.system()
    count_flag = "-n" if system == "Windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", count_flag, "1", "-w", "1000", str(ip)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(str(ip))[0]
            except socket.herror:
                hostname = "Unknown"
            alive_hosts.append((str(ip), hostname))
    except Exception:
        pass

def get_mac(ip):
    system = platform.system()
    arp_cmd = ["arp", "-a"] if system == "Windows" else ["arp", "-n"]

    try:
        arp_output = subprocess.check_output(arp_cmd, encoding="utf-8")
        lines = arp_output.splitlines()
        for line in lines:
            if ip in line:
                mac_match = re.search(r"([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}", line)
                if mac_match:
                    return mac_match.group(0)
    except Exception:
        pass
    return "N/A"

def scan_subnet(subnet):
    print(f"🔍 Scanare în rețeaua: {subnet}")
    threads = []
    for ip in subnet.hosts():
        t = threading.Thread(target=ping, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Așteptăm ca sistemul să actualizeze tabela ARP
    time.sleep(1)

    print("\n📋 Dispozitive detectate:")
    print(f"{'Status':<3} {'IP':<16} {'Host':<30} {'MAC':<20}")
    print("-" * 80)
    for ip, name in sorted(alive_hosts):
        mac = get_mac(ip)
        print(f"🔵  {ip:<16} {name:<30} {mac:<20}")

if __name__ == "__main__":
    try:
        subnet = get_active_subnet()
        scan_subnet(subnet)
    except Exception as e:
        print(f"❌ Eroare: {e}")
