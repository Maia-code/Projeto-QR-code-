import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants,
    box_size=30,
    border=3,
)

qr.add_data('Gerador de QRCode py')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')