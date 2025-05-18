# 🛰️ DNS Sniffer in Python

This is a lightweight DNS sniffer written in Python using the `scapy` library. It listens to DNS queries on a given interface and logs the domains being requested in real time.

⚠️ **Disclaimer**: This tool is for educational and authorized penetration testing use only. Intercepting traffic without consent may violate laws.

---

## 🔍 Features

- Captures DNS queries (UDP port 53)
- Displays queried domains and source IPs
- Lightweight and easy to run on any Linux system
- 
## Usage 

```
usage: DnSniffer.py [-h] --targetip TARGETIP --iface IFACE --routerip ROUTERIP
DnSniffer.py: error: the following arguments are required: --targetip, --iface, --routerip
```
---

## 🛠️ Requirements

- Python 3.x
- `scapy` library
- Root privileges (to sniff packets)

Install dependencies:

```bash
pip install scapy
