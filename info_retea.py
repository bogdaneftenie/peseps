import sys
import os
import socket
import platform
import urllib.request

# ======= Verificare psutil =======
try:
    import psutil
except ImportError:
    print("\033[91m❌ Modulul 'psutil' nu este instalat.\033[0m")
    sugestie = "pip install psutil" if sys.platform.startswith("win") else "pip3 install psutil"
    print(f"🔧 Instalează-l cu comanda: \033[93m{sugestie}\033[0m")
    sys.exit(1)

# ======= Utilitare culori =======
def supports_color():
    if not sys.stdout.isatty():
        return False
    if os.name == 'nt':
        return True
    return True

USE_COLOR = supports_color()

class C:
    VERDE = "\033[92m" if USE_COLOR else ""
    GALBEN = "\033[93m" if USE_COLOR else ""
    ROSU = "\033[91m" if USE_COLOR else ""
    RESET = "\033[0m" if USE_COLOR else ""

def color(text, culoare):
    return f"{culoare}{text}{C.RESET}" if USE_COLOR else text

# ======= Funcții rețea =======
def get_public_ip():
    try:
        with urllib.request.urlopen("https://api.ipify.org", timeout=5) as response:
            return response.read().decode()
    except Exception:
        return "Nedisponibil"

def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "Nedisponibil"

def get_active_mac():
    try:
        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == psutil.AF_LINK or getattr(socket, 'AF_PACKET', None) == addr.family:
                    if "00:00:00" not in addr.address and len(addr.address) == 17:
                        return addr.address
    except Exception:
        pass
    return "Neprecizat"

def system_info():
    return f"{platform.system()} {platform.release()} ({platform.machine()})"

# ======= Main =======
def main():
    hostname = socket.gethostname()

    print(color("📡 Informații conexiune rețea:", C.GALBEN))
    print("-" * 40)
    print(f"🔠 Nume Host       : {color(hostname, C.GALBEN)}")
    print(f"🌐 IP Public       : {color(get_public_ip(), C.VERDE)}")
    print(f"🏠 IP Local        : {color(get_local_ip(), C.VERDE)}")
    print(f"🔌 MAC Activ       : {color(get_active_mac(), C.GALBEN)}")
    print(f"🖥️  Sistem         : {color(system_info(), C.GALBEN)}")
    print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(color("\n⛔ Întrerupt de utilizator.", C.ROSU))
        sys.exit(1)
