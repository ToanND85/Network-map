import csv
from pathlib import Path


def read_devices(file_path):
    """Doc danh sach thiet bi tu CSV."""
    with open(file_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def count_status(devices):
    """Thong ke so thiet bi Online va Offline."""
    total = len(devices)
    online = sum(
        1 for d in devices
        if d["Status"].strip().lower() == "online"
    )
    offline = sum(
        1 for d in devices
        if d["Status"].strip().lower() == "offline"
    )

    return total, online, offline


def get_offline_devices(devices):
    """Lay danh sach thiet bi Offline."""
    return [
        d for d in devices
        if d["Status"].strip().lower() == "offline"
    ]


def main():
    file_path = Path(__file__).parent / "devices.csv"

    devices = read_devices(file_path)
    total, online, offline = count_status(devices)

    print("=== NETWORK MONITOR ===")
    print(f"Tong so thiet bi: {total}")
    print(f"Online: {online}")
    print(f"Offline: {offline}")

    print("\nDanh sach thiet bi Offline:")

    for device in get_offline_devices(devices):
        print(
            f"- {device['Device_Name']} "
            f"| IP: {device['IP_Address']} "
            f"| Location: {device['Location']}"
        )


if __name__ == "__main__":
    main()