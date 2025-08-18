import qrcode
from PIL import Image

# Data to encode
data = "https://hackthenorth.com/crystalcavern.pdf"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create image in black-and-white mode
img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Make white pixels transparent
datas = img.getdata()
new_data = []

for item in datas:
    # item is (R, G, B, A)
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        # Make white pixels fully transparent
        new_data.append((255, 255, 255, 0))
    else:
        # Keep black pixels
        new_data.append(item)

img.putdata(new_data)

# Save image
img.save("qr_transparent.png")
