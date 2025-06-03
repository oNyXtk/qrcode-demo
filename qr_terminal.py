import qrcode

# Terminal QR
qr = qrcode.QRCode()
qr.add_data("https://www.python.org")
qr.make()
qr.print_ascii()
