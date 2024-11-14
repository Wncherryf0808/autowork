import time

def run():
    print("111")
    time.sleep(10)
    raise Exception("错误验证")


run()