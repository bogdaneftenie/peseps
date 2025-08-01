import socket
import datetime
import os
import sys

# ======= CONFIG =======
TEST_HOST = os.getenv("CHECK_HOST", "8.8.8.8")
TEST_PORT = int(os.getenv("CHECK_PORT", "53"))
TIMEOUT = int(os.getenv("CHECK_TIMEOUT", "3"))
LOG_FILE_NAME = os.getenv("LOG_FILE", "log_conexiune.txt")
LOG_DIR = os.getenv("LOG_DIR", os.path.join(os.path.expanduser("~"), "Desktop"))

if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
    except Exception as e:
        print(f"Warning: nu s-a putut crea directorul de log: {LOG_DIR} ({e})")
        LOG_DIR = os.path.expanduser("~")  # fallback

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# ======= UTILITĂȚI CULORI; =======
def supports_color():
    if not sys.stdout.isatty():
        return False
    if os.name == 'nt':
        # pe Windows, dacă e Windows 10+ probabil funcționează
        return True
    # alte sisteme
    return True

USE_COLOR = supports_color()

class Culori:
    VERDE = "\033[92m" if USE_COLOR else ""
    GALBEN = "\033[93m" if USE_COLOR else ""
    ROSU = "\033[91m" if USE_COLOR else ""
    RESET = "\033[0m" if USE_COLOR else ""

def color(text, culoare):
    return f"{culoare}{text}{Culori.RESET}" if USE_COLOR else text

# ======= VERIFICARE CONEXIUNE =======
def verifica_conexiune(host=TEST_HOST, port=TEST_PORT, timeout=TIMEOUT):
    try:
        socket.setdefaulttimeout(timeout)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
        return True
    except socket.error:
        return False

# ======= LOGARE =======
def log_conexiune(stare, log_path=LOG_FILE_PATH):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mesaj = f"[{timestamp}] Stare conexiune: {stare}\n"

    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(mesaj)
        print(color(f"📝 Log salvat: {log_path}", Culori.GALBEN))
    except Exception as e:
        print(color(f"❌ Eroare la scrierea logului: {e}", Culori.ROSU))

# ======= MAIN =======
def main():
    print(color(f"🌐 Verific conexiunea catre INTERNET ...", Culori.GALBEN))
    online = verifica_conexiune()
    stare = "ONLINE" if online else "OFFLINE"
    culoare_stare = Culori.VERDE if online else Culori.ROSU
    print(color(f"✅ Conexiune: {stare}", culoare_stare))
    log_conexiune(stare)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(color("\n⛔ Întrerupt de utilizator.", Culori.ROSU))
        sys.exit(1)
