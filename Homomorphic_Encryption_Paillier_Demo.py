

from phe import paillier

# Generate public and private key pair
public_key, private_key = paillier.generate_paillier_keypair()

# Encrypt two numbers
plaintext1 = 42
plaintext2 = 99
ciphertext1 = public_key.encrypt(plaintext1)
ciphertext2 = public_key.encrypt(plaintext2)

# Display encrypted values
print("Encrypted value 1:", ciphertext1.ciphertext())
print("Encrypted value 2:", ciphertext2.ciphertext())

# Perform homomorphic addition on ciphertexts
ciphertext_sum = ciphertext1 + ciphertext2

# Decrypt the result
decrypted_sum = private_key.decrypt(ciphertext_sum)
print("Decrypted sum:", decrypted_sum)
