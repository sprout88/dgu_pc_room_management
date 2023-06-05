import pywin32_draw
import pyautogui as p
from PIL import Image
import time
import os
import keyboard
import shutil
import requests

print("ubuntu 다운로드 시도...")
url = "https://ftp.lanet.kr/ubuntu-releases/22.04.2/ubuntu-22.04.2-desktop-amd64.iso"
filename = "myfile.zip"

with open(filename, 'wb') as f:
  res = requests.get(url, stream=True)
  r_bytes : int = 0
  t_bytes : int = int(res.headers.get('Content-Length', 0))
  for chunk in res.iter_content(1024):
    f.write(chunk)
    r_bytes += len(chunk)
    print(f"\r req url : {url} downloading... : {r_bytes / t_bytes : .2%}", end="")
print("\rubuntu 다운로드 완료!")