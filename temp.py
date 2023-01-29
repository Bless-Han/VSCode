import os
import qrcode

img = qrcode.make("https://www.bing.com")

img.sae("qr.png", "PNG")

os.system("open qr.png")