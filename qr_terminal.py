import qrcode
# qr_terminal.py
# Teek: qrcode
# Kirjeldus: prindib QR-koodi otse terminali ASCII kujul (ei loo pilti)
# Terminal QR
qr = qrcode.QRCode()
qr.add_data("https://www.python.org")
qr.make()
qr.print_ascii()
