import qrcode


data = "https://www.wikipedia.org"
qr = qrcode.make(data)
qr.save("wikipedia_qr.png")
