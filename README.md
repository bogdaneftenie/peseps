# 🌐 peseps – Scripturi utile pentru testare rețea

Acest repository conține scripturi Python compatibile cu **Windows și Linux**, pentru verificarea conexiunii la internet, informații despre rețea și testare cu `ping`. Toate scripturile sunt simple, portabile și utile pentru depanare.

---

## 📝 Scripturi disponibile

| Script              | Descriere                                                                                                                      | Cum se rulează                            |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `test_conexiune.py` | Verifică dacă există conexiune reală la internet printr-un **socket TCP către `8.8.8.8:53` (DNS)**. Nu folosește `ping`. Salvează logul într-un fișier pe Desktop. | `python test_conexiune.py` |
| `ping_report.py`    | Trimite `ping` către mai multe destinații (`8.8.8.8`, `google.com`, etc.), afișează rezultatele și salvează un log CSV pe Desktop. | `python ping_report.py`    |
| `info_retea.py`     | Afișează IP-ul public, IP-ul local, MAC-ul activ, sistemul de operare și numele hostului. Necesită `psutil` și `requests`. | `python info_retea.py`     |

> ⚠️ `test_conexiune.py` nu folosește `ping`, ci un **socket TCP** – metodă mai fiabilă în rețele cu firewall-uri stricte sau ICMP blocat.

---

## 🧰 Cerințe

- ✅ Python 3.x instalat
- 💻 Funcționează pe Windows și Linux
- 📦 Nu necesită biblioteci externe (cu excepția `info_retea.py`, care are nevoie de:  
  ```bash
  pip install psutil requests
  ```  
  )

---

## 📂 Loguri generate

- `test_conexiune.py`: salvează un fișier `log_conexiune.txt` pe Desktop, cu istoricul stării rețelei.
- `ping_report.py`: salvează un fișier `ping_log.csv` pe Desktop, cu timpul de răspuns pentru fiecare destinație testată.

---

## 📌 Sugestii

- Poți configura comportamentul scripturilor folosind **variabile de mediu**:  
  `CHECK_HOST`, `CHECK_PORT`, `LOG_DIR`, `CHECK_TIMEOUT` etc.
- Scripturile pot fi folosite cu **cron** (Linux) sau **Task Scheduler** (Windows) pentru monitorizare automată.
- Logurile sunt scrise în folderul Desktop pentru acces rapid, dar poți schimba locația prin `LOG_DIR`.

---

## 📁 Structura proiectului

```
peseps/
├── test_conexiune.py
├── ping_report.py
├── info_retea.py
└── README.md
```

---

## 🤝 Contribuții

Poți propune noi scripturi sau optimizări. Repository-ul e gândit să crească – **contribuțiile sunt binevenite**. Deschide un *issue* sau trimite un *pull request*.

---

## 🔒 Licență

📜 Proiect open-source – îl poți **folosi**, **adapta** și **distribui** liber. Fără restricții comerciale.  
Distribuit sub licența MIT.

---
