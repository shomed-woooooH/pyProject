import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H)
qr.add_data('https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=1')
qr.make(fit= True)

img = qr.make_image(fill_color = 'white',back_color = 'black')
img.save('rian.jpg')
