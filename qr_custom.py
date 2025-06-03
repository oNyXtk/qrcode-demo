import qrcode

# qr_custom.py
# Teek: qrcode
# Kirjeldus: loob kohandatud QR-koodi (suurus, servad, värv, veaparandus)
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data("https://chat.openai.com")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("chatgpt_qr.png")
