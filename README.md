# 🌐 Network Utility Scripts

This repository contains simple and cross-platform Python scripts for basic **network diagnostics** and **connectivity monitoring**. All scripts are tested on both **Windows** and **Linux**.

---

## 📜 Available Scripts

| Script              | Description                                                                                       | How to Run                          |
|---------------------|---------------------------------------------------------------------------------------------------|-------------------------------------|
| `test_connection.py` | Checks if the system has real internet access using a **TCP socket to `8.8.8.8:53` (DNS)**. No `ping`. Saves a log file. | `python test_connection.py`         |
| `ping_report.py`     | Pings multiple destinations (`8.8.8.8`, `google.com`, etc.), prints the result and saves a CSV log. | `python ping_report.py`             |
| `network_info.py`    | Displays the **external IP**, **active network interface**, **MAC address**, and hostname.       | `python network_info.py`            |

> ⚠️ `test_connection.py` avoids using `ping` and instead relies on a **reliable TCP socket test**, which works even in restrictive network environments (e.g. firewalled ICMP).

---

## 🧰 Requirements

- Python **3.x** installed
- Scripts work on **Windows** and **Linux**
- Only one script (`network_info.py`) requires the external module `psutil` (see below)

---

## 📂 Logs Generated

| Script              | Output File                         | Location     |
|---------------------|--------------------------------------|--------------|
| `test_connection.py` | `log_connection.txt` (text format)   | Saved to Desktop |
| `ping_report.py`     | `ping_log.csv` (CSV format)          | Saved to Desktop |

---

## ⚙️ Configurability

Some scripts accept configuration via **environment variables**:

| Variable        | Description                         | Example              |
|------------------|-------------------------------------|-----------------------|
| `CHECK_HOST`      | IP or hostname to check connection | `8.8.4.4`             |
| `CHECK_PORT`      | Port number for socket check       | `53`                  |
| `LOG_DIR`         | Where to save log files            | `/home/user/logs`     |

These variables are **optional**. Default values are used if they are not set.

---

## 🧱 Folder Structure

```
peseps/
├── test_connection.py     # Checks internet via TCP socket
├── ping_report.py         # Pings multiple addresses and logs
├── network_info.py        # Shows external IP, MAC, interface
└── README.md              # Project documentation
```

---

## 💡 Tips

- Scripts can be scheduled via:
  - `cron` (Linux/macOS)
  - `Task Scheduler` (Windows)
- Useful for **offline diagnostics**, **monitoring**, or **network logging**.

---

## 🤝 Contributing

Want to add new features or scripts? Contributions are welcome!

- Fork this repo
- Submit a pull request
- Or open an issue with ideas or improvements

---

## 🔒 License

This project is open-source and distributed under the **MIT License**. Use, modify, and share freely.

---

## 📞 Contact

Made with 💻 by [Bogdan Eftenie](https://github.com/bogdaneftenie)
