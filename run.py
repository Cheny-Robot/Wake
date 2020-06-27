import requests
import sys
import time

i = 0
urls = sys.argv[1].split(',') if len(sys.argv) >= 2 else ['https://www.antmoe.com/']
for url in urls:
    req = requests.get(url)
    print(f'第{i}号网址唤醒状态:', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    i = i+1
