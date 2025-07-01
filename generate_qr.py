import qrcode
import time

timestamp = int(time.time())
url = f"https://example.com/?t={timestamp}"
img = qrcode.make(url)
img.save(f"qr_{timestamp}.png")
