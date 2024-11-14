from airtest.core.api import *

from scripts.common.util import get_android_devices

class App:
    def __init__(self, packagename):
        self.dev = connect_device("Android:///")
        self.packagename = packagename

    def install_app(self, path):
        """安装"""
        self.dev.install_app(path)

    def start_app(self):
        """启动"""
        self.dev.start_app(self.packagename)

    def stop_app(self):
        """停止"""
        self.dev.stop_app(self.packagename)

    def uninstall_app(self):
        """卸载"""
        self.dev.uninstall_app(self.packagename)


