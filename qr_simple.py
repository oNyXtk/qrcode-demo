import qrcode
# qr_simple.py
# Teek: qrcode
# Kirjeldus: loob lihtsa QR-koodi Wikipedia lingile ja salvestab selle pildina

data = "https://www.wikipedia.org"
qr = qrcode.make(data)
qr.save("wikipedia_qr.png")
