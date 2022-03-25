print("RSA:");
# the message
m=6

#public key
e=5
n=119

#private key
d=77

# encryption
cipher=pow(m,e) % n
print ("\nThe ciphertext is:", cipher)

# decryption
plain=pow(cipher,d) % n
print ("The plaintext is:", plain)