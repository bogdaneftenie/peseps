import platform
import subprocess
import csv
import datetime
import os
import sys

# ========= CONFIG =========
DESTINATII = ["8.8.8.8", "1.1.1.1", "google.com", "cloudflare.com"]
NUMAR_PING = 3  # pings per destinație
TIMEOUT_SEC = 2

# Detectăm sistemul
IS_WINDOWS = platform.system().lower() == "windows"

# ========= CULOARE; =========
def supports_color():
    return sys.stdout.isatty()

class Culoare:
    VERDE = "\033[92m" if supports_color() else ""
    ROSU = "\033[91m" if supports_color() else ""
    GALBEN = "\033[93m" if supports_color() else ""
    RESET = "\033[0m" if supports_color() else ""

def color(text, culoare):
    return f"{culoare}{text}{Culoare.RESET}"

# ========= FUNCȚIE PING =========
def ping_host(host):
    if IS_WINDOWS:
        cmd = ["ping", "-n", str(NUMAR_PING), "-w", str(TIMEOUT_SEC * 1000), host]
    else:
        cmd = ["ping", "-c", str(NUMAR_PING), "-W", str(TIMEOUT_SEC), host]

    try:
        rezultat = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_SEC * NUMAR_PING + 2)
        output = rezultat.stdout

        success = "TTL=" in output or "ttl=" in output or "bytes from" in output
        time_lines = [line for line in output.splitlines() if "time=" in line]

        if time_lines:
            # Extragem timpul mediu
            times = []
            for line in time_lines:
                parts = line.split("time=")
                if len(parts) > 1:
                    val = parts[1].split()[0].replace("ms", "")
                    try:
                        times.append(float(val))
                    except ValueError:
                        continue
            avg_time = round(sum(times) / len(times), 2) if times else None
        else:
            avg_time = None

        return success, avg_time

    except subprocess.TimeoutExpired:
        return False, None

# ========= LOGARE CSV =========
def log_to_csv(rows):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    log_file = os.path.join(desktop, "ping_log.csv")
    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Timp", "Destinație", "Status", "Timp Mediu (ms)"])
        writer.writerows(rows)

# ========= MAIN =========
def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(color(f"\n🌐 Pornesc testele de ping ({timestamp})...\n", Culoare.GALBEN))
    
    log_data = []

    for host in DESTINATII:
        print(color(f"🔄 Testez {host} ...", Culoare.GALBEN))
        success, avg_time = ping_host(host)

        if success:
            msg = f"✅ ONLINE - {host} răspunde (~{avg_time} ms)"
            print(color(msg, Culoare.VERDE))
            log_data.append([timestamp, host, "ONLINE", avg_time])
        else:
            print(color(f"❌ OFFLINE - {host} nu răspunde", Culoare.ROSU))
            log_data.append([timestamp, host, "OFFLINE", "N/A"])

    # salvare log
    log_to_csv(log_data)
    print(color("\n📝 Log salvat pe Desktop în 'ping_log.csv'\n", Culoare.GALBEN))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(color("\n⛔ Oprit de utilizator.", Culoare.ROSU))
