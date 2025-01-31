# 🕵️‍♂️ Network Scanner Tool  

## 📜 Description  
This Python tool leverages the **Scapy** library to perform **ARP scanning** on a network. It is used to discover active devices on a given IP range or target IP address by sending ARP requests and collecting responses. This tool can be helpful for network reconnaissance, device inventory management, or penetration testing purposes.

---

## 🚀 Features  
- Scans a specified IP address or IP range to detect active devices.
- Retrieves the **IP address** and **MAC address** of each detected device.
- Outputs results in a readable format showing the IP and MAC address pairs.

---

## 🛠️ Prerequisites  
Before running the script, make sure you have:
- **Python 3.x** installed.
- **Scapy** library installed:
    ```bash
    pip install scapy
    ```

This script is designed for **Linux** and other Unix-like operating systems.

---

## 🎯 Usage  

### **1. Running the Network Scanner**

To use the tool, you need to specify the target IP address or IP range. The script supports **CIDR notation** (e.g., `192.168.1.0/24`) for IP ranges.

#### **Command-line Arguments:**  
- `-t, --target`: The target IP address or IP range you want to scan for active devices.

#### **Example Usage:**  
```bash
sudo python3 network_scanner.py -t 192.168.1.0/24
```
## Output
```bash
IP				MAC
----------------------------------------------
192.168.1.1		00:11:22:33:44:55
192.168.1.2		66:77:88:99:00:11
```
