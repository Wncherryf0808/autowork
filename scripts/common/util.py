from airtest.core.android.adb import ADB

def get_android_devices():
    device_list = []
    devices = ADB().devices()
    for device in devices:
        device_list.append(device[0])

    return device_list
