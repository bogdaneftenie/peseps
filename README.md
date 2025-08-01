# 🧪 Network Tools Collection

A set of cross-platform Python scripts for checking internet connection, gathering local network data, and basic connectivity monitoring. All tools are designed to run on **Windows** and **Linux** using standard Python libraries (with minimal external dependencies).

---

## 📁 Folder Structure

```
/peseps
│
├── test_conexiune.py       # Internet connectivity check using socket (no ping)
├── ping_report.py          # Ping test to multiple destinations, with CSV logging
├── info_retea.py           # Display external IP, internal IP, MAC address, hostname
├── scan_lan.py             # Scan LAN for connected devices with IP and MAC
├── README.md               # Project documentation (this file)
```

---

## 📜 Available Scripts

| Script              | Description                                                                                 | Run Command                  |
|---------------------|---------------------------------------------------------------------------------------------|------------------------------|
| `test_conexiune.py` | Checks internet connection using TCP socket to `8.8.8.8:53`. Logs result to a `.txt` file.  | `python test_conexiune.py`  |
| `ping_report.py`    | Sends pings to several destinations, logs response times to `.csv` on Desktop.              | `python ping_report.py`     |
| `info_retea.py`     | Displays internal & external IP, hostname, and MAC of the active network interface.         | `python info_retea.py`      |
| `scan_lan.py`       | Scans the local network to detect connected devices, showing IP and MAC addresses.          | `python scan_lan.py`        |

---

## 🧰 Requirements

- Python 3.x installed
- Works on **Windows** and **Linux**
- Requires the `psutil` module (`info_retea.py` only)

```bash
pip install psutil
```

---

## 📂 Log Files

- `test_conexiune.py`: writes `log_conexiune.txt` on the **Desktop** with connection status.
- `ping_report.py`: creates a `ping_log.csv` on the **Desktop** with ping results.
- `scan_lan.py`: optionally prints/export scanned devices.

---

## ⚙️ Environment Variables

You can customize behavior using environment variables:

| Variable       | Default     | Description                          |
|----------------|-------------|--------------------------------------|
| `CHECK_HOST`   | `8.8.8.8`   | Host used in socket test             |
| `CHECK_PORT`   | `53`        | Port used in socket test             |
| `CHECK_TIMEOUT`| `3`         | Timeout in seconds                   |
| `LOG_DIR`      | Desktop     | Where logs are saved                 |

---

## 💡 Suggestions

- You can schedule these scripts with **cron** (Linux) or **Task Scheduler** (Windows).
- Adapt logging directories or output formats depending on your workflow.
- Add automation for alerts (e.g., email or webhook on disconnect).

---

## 🤝 Contributions

Feel free to contribute new tools or improvements – the goal is to expand this repo with useful network utilities. Forks and pull requests are welcome!

---

## 🔒 License

This project is **open-source**, licensed under the MIT license. You’re free to use, modify, and share.

---

## 📬 Contact

For updates, feedback, or ideas, visit: [github.com/bogdaneftenie](https://github.com/bogdaneftenie)
