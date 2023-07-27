import qrcode

print("This program creates a simple qrcode from a URL that you will provide!")

site = str(input("Which URL do you want to put in your qrcode?\n"))
    
def make(site):
    img = qrcode.make(f'{site}')
    type(img)  # qrcode.image.pil.PilImage
    img.save("qrcode.png")
    
print(make(site))