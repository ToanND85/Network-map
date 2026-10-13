
import csv
from pathlib import Path

# Xac dinh duong dan file CSV
file_path = Path(__file__).parent / "devices.csv"

# Doc danh sach thiet bi
with open(file_path, mode="r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    devices = list(reader)

# Thong ke trang thai
total = len(devices)
online = sum(1 for d in devices if d["Status"].strip().lower() == "online")
offline = sum(1 for d in devices if d["Status"].strip().lower() == "offline")

# Hien thi ket qua
print("=== NETWORK MONITOR ===")
print(f"Tong so thiet bi: {total}")
print(f"Online: {online}")
print(f"Offline: {offline}")

print("\nDanh sach thiet bi Offline:")

for device in devices:
    if device["Status"].strip().lower() == "offline":
        print(
            f"- {device['Device_Name']} "
            f"| IP: {device['IP_Address']} "
            f"| Location: {device['Location']}"
        )
