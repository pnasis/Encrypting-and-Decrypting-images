# Opening and reading the encrypted image
file = open('encrypted.jpg', "rb")
encrypted_image = file.read()
file.close()

# Converting the encrypted image into a bytearray using the same key value (48)
encrypted_image = bytearray(encrypted_image)
key = 48

# Decrypting the image
for i, j in enumerate(encrypted_image):
    encrypted_image[i] = j ^ key

# Creating the new decrypted image
file = open('decrypted.jpg', "wb")
file.write(encrypted_image)
file.close()
