# Opening and reading the image
file = open('image.jpg', "rb")
image = file.read()
file.close()

# Converting the image into a bytearray using the value 48 as the key
image = bytearray(image)
key = 48

# Encrypting the image
for i, j in enumerate(image):
    image[i] = j ^ key

# Creating the new encrypted image
file = open('encrypted.jpg', "wb")
file.write(image)
file.close()
