# wifi_qrcode.py
# Version 1.0
# Written by Anthony Carlson 6/1/2022

import pyqrcode
from PIL import Image

ssid = input("Enter SSID: ")
password = input("Enter WiFi Password: ")
security = input("Security Type (WPA or WEP): ")
extension=".png"
output = "".join([ssid,extension])

qr = pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
qr.png(output,scale=8)