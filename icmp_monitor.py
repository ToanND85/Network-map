
import csv
import subprocess
from pathlib import Path

csv_path = Path(__file__).parent / "devices.csv"

def ping_device(ip):
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", ip],
        capture_output=True,
        text=True,
        errors="replace"
    )
    return result.returncode == 0

with open(csv_path, encoding="utf-8-sig", newline="") as file:
    devices = list(csv.DictReader(file))

print("=== ICMP NETWORK MONITOR ===")

for device in devices:
    name = device["Device_Name"]
    ip = device["IP_Address"]

    reachable = ping_device(ip)
    status = "REACHABLE" if reachable else "NO RESPONSE"

    print(f"{name:20} {ip:16} {status}")
