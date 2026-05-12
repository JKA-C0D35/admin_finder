# 🔍 Admin Finder

A multithreaded Python-based admin panel finder for educational and authorized security testing purposes.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Threads](https://img.shields.io/badge/Threading-Enabled-red?style=for-the-badge)

---

## 📌 Description

**Admin Finder** is a lightweight Python tool that scans websites for common admin panel paths using multithreading and randomized User-Agent headers.

The project demonstrates:
- HTTP requests
- Python threading
- Basic reconnaissance techniques
- Error handling
- Automation scripting

---

## ⚡ Features

- Multi-threaded scanning
- Random User-Agent rotation
- Fast admin path detection
- Handles connection errors
- Beginner-friendly Python code
- Easy to customize

---

## 🛠️ Built With

- Python 3
- `requests`
- `threading`
- `random`
- `time`

---

## 📂 Admin Paths Included

```txt
/admin
/admin/login
/admin/dashboard
/administrator
/cpanel
/dashboard
/backend
/webadmin
/siteadmin
```

And many more...

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/JKA-C0D35/admin-finder.git
cd admin-finder
```

Install required modules:

```bash
pip install requests
```

---

## ▶️ Usage

Run the script:

```bash
python admin_finder.py
```

Enter a target URL:

```bash
Target URL: https://example.com
```

---

## 🖥️ Example Output

```bash
Scanning: https://example.com

Status: 200 | URL: https://example.com/admin
Status: 404 | URL: https://example.com/admin/login
[ERROR]: https://example.com/cpanel -> Connection timed out
```

---

## 📁 Project Structure

```txt
admin-finder/
│
├── admin_finder.py
├── README.md
├── LICENSE
├── requirements.txt
```

---

## 🧠 What I Learned

This project helped improve my understanding of:

- Python threading
- HTTP requests
- Response status handling
- Web path scanning
- Automation scripting
- Exception handling

---

## ⚠️ Disclaimer

This tool is created for:

- Educational purposes
- Ethical hacking practice
- Authorized penetration testing only

Do not use this tool against websites without permission.


[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&width=435&lines=%3E+BOOTING+PROFILE...++%5BIDENTITY%5D+Hello+%F0%9F%91%8B+I'm+JKA-C0D35++%5BROLE%5D+Python+Developer+%E2%9A%99%EF%B8%8F+Backend+Developer+(In+Progress)+%F0%9F%92%BB+Cybersecurity+Developer+%7C+Ethical+Hacking+Enthusiast+%F0%9F%94%90++%5BMISSION%5D+Building+tools+%E2%80%A2+Breaking+limits+%E2%80%A2+Learning+systems+%F0%9F%9A%80++%5BSTATUS%5D+Always+learning.+Always+improving.+Always+building+%F0%9F%92%A1++%3E+SYSTEM+READY...)](https://git.io/typing-svg)
---

## 👨‍💻 Author

**JKA-C0D35**

Cybersecurity & Python Beginner 🚀
