import requests
import sys
import time

urls = sys.argv[1].split(',') if len(sys.argv) >= 2 else ['https://www.antmoe.com/']
for i in range(0, len(urls)):
    print(f'第{i}号网址唤醒状态:', requests.get(urls[i]), time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
