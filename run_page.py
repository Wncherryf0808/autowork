"""启动页"""
import os.path
import unittest

from airtest.core.android.adb import ADB
from airtest.core.api import *
from airtest.cli.parser import cli_setup

from scripts.common.app_control import App

# 初始化环境接口，自动配置运行环境，如果当前没有链接设备的话，就默认尝试连接Android设备
# 设置当前脚本所在的路径，静定运行脚本的设备，设置默认的log路径，设置脚本父路径和屏幕的压缩比
# 不设置参数的话，Airtest 会读取运行时命令行传入的各项参数，来对环境进行初始化。
# 要尽量在脚本初始化期间调用 auto_setup 接口，保证尽可能争取初始化环境/并生成 log 文件，否则不会生成 log 内容
auto_setup(__file__)
dev = connect_device("Android:///")


class AutoTest(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.app = App("cn.jj.mahjong")
        self.fPy = r"J:\autowork\scripts\case\test_demo\test_demo.py."

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.app.install_app(r"C:\Users\wanghp\Downloads\JJMaj.51901.53300.dcf9c3d4e75b7108ff498cb8d9535278.bit64.apk")
        self.app.start_app()
        # 初始化APP
        with open(self.fPy, 'r', encoding='utf-8') as f:
            code = f.read()
            # compile 用于将源代码编译为字节码对象，这个字节码对下可以被exec()或eval()函数执行，它提供了一种在运行时动态编译代码的方式
            # 对于一些需要根据不同情况生成和执行代码的场景非常有用
        self.code = compile(code.encode('utf-8'), self.fPy, "exec")

    def tearDown(self):
        self.app.stop_app()
        self.app.uninstall_app()

    def runTest(self):
        ns = {"__file__": self.fPy}
        # exec 动态执行Python代码
        exec(self.code, ns)

def new_case():
    auto_test = AutoTest()
    # os.path.basename 返回路径中的文件名部分 /home/user/Documents/example.txt    example.txt
    sPyFileName = os.path.basename(AutoTest().fPy).replace("py", "")
    # 去文件的文件名 和 文件路径
    return auto_test

def run_scripts():
    # 添加用例组
    test_suite = unittest.TestSuite()
    case = new_case()
    test_suite.addTest(case)
    # 执行用例
    unittest.TextTestRunner().run(test_suite)

def main():
    run_scripts()


if __name__ == '__main__':
    main()

