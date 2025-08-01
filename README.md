# 🛠️ peseps - Colecție de Scripturi pentru Monitorizarea Rețelei

Acest repository conține scripturi simple și eficiente scrise în Python, utile pentru verificarea conexiunii la internet și monitorizarea răspunsurilor de la diverse destinații.

---

## 📜 Scripturi disponibile

| Script             | Descriere                                                                                                         | Cum se rulează                            |
|--------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `test_conexiune.py` | Verifică dacă există conexiune reală la internet printr-un **socket TCP către `8.8.8.8:53` (DNS)**. Nu folosește `ping`. Salvează logul într-un fișier pe Desktop. | `python test.py`                |
| `ping_report.py`    | Trimite `ping` către mai multe destinații (`8.8.8.8`, `google.com`, etc.), afișează rezultatele și salvează un log CSV pe Desktop.                     | `python ping_report.py`                   |

> ⚠️ `test_conexiune.py` nu folosește `ping`, ci un socket TCP pentru a verifica conectivitatea – o metodă mai fiabilă în rețele cu firewall-uri stricte.

---

## 🧰 Cerințe

- Python 3.x instalat
- Funcționează pe **Windows și Linux**
- Nu necesită biblioteci externe (doar module standard Python)

---

## 📂 Loguri generate

- `test_conexiune.py`: salvează un fișier text `log_conexiune.txt` pe Desktop, cu istoricul stării rețelei.
- `ping_report.py`: salvează un fișier `ping_log.csv` pe Desktop, cu timpul de răspuns pentru fiecare destinație testată.

---

## 📌 Sugestii

- Poți configura comportamentul scripturilor folosind variabile de mediu:
  - `CHECK_HOST`, `CHECK_PORT`, `LOG_DIR` etc.
- Scripturile pot fi folosite în cron (Linux) sau Task Scheduler (Windows) pentru monitorizare automată.

---

## 🤝 Contribuții

Poți propune noi scripturi sau optimizări. Repository-ul e gândit să crească – contribuțiile sunt binevenite.

---

## 🔒 Licență

Proiect open-source – îl poți folosi, adapta și distribui liber.


