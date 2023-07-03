# Encrypting and Decrypting images

1. **Encryptor Program:**
The encryptor program is designed to encrypt .jpg and .png image files found in specified directories. It takes each image file, reads its content as a byte array, and applies a bitwise XOR operation with a key value. This process effectively encrypts the image by altering the byte values. The encrypted image is then saved as a new file with "_encrypted" appended to the original filename. Finally, the original image file is deleted, ensuring only the encrypted version remains.

2. **Decryptor Program:**
The decryptor program is intended to decrypt the images that were encrypted using the encryptor program. It searches for image files with "_encrypted.jpg" or "_encrypted.png" extensions in the specified directories. For each encrypted image, it reads the file content as a byte array and performs the bitwise XOR operation with the same key value used during encryption. This reverses the encryption process and restores the original image. The decrypted image is saved as a new file with "_decrypted" added to the original filename. Finally, the encrypted file is deleted from the system.

Both programs operate on the principle of bitwise XOR encryption, where the key value is used to modify the byte values of the image files. It's important to note that these programs assume proper authorization and permissions to access and modify the files. Additionally, both encryptor and decryptor program include code to delete themselves after completing the encryption and decryption processes, ensuring that the programs are removed from the system once their purpose is fulfilled.

## Usage
**To run the `encryptor.py` program:**
```bash
# To run the encryptor program
python3 encryptor.py
```

**To run the `decryptor.py` program:**
```bash
# To run the decryptor program
python3 decryptor.py
```

## Contributing

>Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

>This project is under [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) licence.
