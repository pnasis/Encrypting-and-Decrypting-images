#opening and saving the image
file = open('image.jpg', "rb")
image = file.read()
file.close()

#converting the image into a bytearray using as key the value 48
image = bytearray(image)
key = 48

#conversion on the image
for i,j in enumerate(image):
    image[i] =j^key

#creating the new encrypted image
file = open('encrypted.jpg', "wb")
file.write(image)
file.close()

#If you want to decrypt the image, you change the first patameter in line 2 with the name of the image you want to decrypt, and the first
#parameter in line 15 with the name that the new decrypted image you want to have.