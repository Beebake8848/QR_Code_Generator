import qrcode

data = "https://facebook.com"
file_name = "qrcode.png"

qrcode.make(data).save(file_name)

print("QR code generated successfully!")
