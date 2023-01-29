import os
import qrcode

img = qrcode.make("https://www.bing.com")

img.save("qr.png", "PNG")

os.system("open qr.png")