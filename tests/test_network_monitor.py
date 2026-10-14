import importlib.util
from pathlib import Path

# Nap module Network-monitor.py (ten file co dau gach ngang)
PROJECT_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_DIR / "Network-monitor.py"

spec = importlib.util.spec_from_file_location(
    "network_monitor", MODULE_PATH
)
network_monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(network_monitor)


def test_read_devices():
    """Kiem tra doc du 6 thiet bi tu CSV."""
    devices = network_monitor.read_devices(
        PROJECT_DIR / "devices.csv"
    )

    assert len(devices) == 6
    assert devices[0]["Device_Name"] == "OLT-01"


def test_count_status():
    """Kiem tra thong ke Online/Offline."""
    devices = network_monitor.read_devices(
        PROJECT_DIR / "devices.csv"
    )

    total, online, offline = network_monitor.count_status(devices)

    assert total == 6
    assert online == 5
    assert offline == 1


def test_get_offline_devices():
    """Kiem tra loc dung thiet bi Offline."""
    devices = network_monitor.read_devices(
        PROJECT_DIR / "devices.csv"
    )

    offline_devices = network_monitor.get_offline_devices(devices)

    assert len(offline_devices) == 1
    assert offline_devices[0]["Device_Name"] == "OLT-02"
    assert offline_devices[0]["IP_Address"] == "192.0.2.40"


def test_status_case_insensitive():
    """Kiem tra xu ly chu hoa, chu thuong va khoang trang."""
    devices = [
        {"Status": " ONLINE "},
        {"Status": "offline"},
        {"Status": "Online"},
    ]

    total, online, offline = network_monitor.count_status(devices)

    assert (total, online, offline) == (3, 2, 1)


def test_empty_device_list():
    """Kiem tra danh sach thiet bi rong."""
    devices = []

    assert network_monitor.count_status(devices) == (0, 0, 0)
    assert network_monitor.get_offline_devices(devices) == []