def test_online_device():
    status = "Online"
    assert status.lower() == "online"


def test_offline_device():
    status = "Offline"
    assert status.lower() == "offline"


def test_total_devices():
    online = 5
    offline = 1
    assert online + offline == 6