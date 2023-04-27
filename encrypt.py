# import tkinter as tk

# from Crypto.Cipher import AES
# import base64, os


# def encrypt_message(private_msg, encoded_secret_key, padding_character):
# 	# decode the encoded secret key
# 	secret_key = base64.b64decode(encoded_secret_key)
# 	# use the decoded secret key to create a AES cipher
# 	cipher = AES.new(secret_key, AES.MODE_ECB)
# 	# pad the private_msg
# 	# because AES encryption requires the length of the msg to be a multiple of 16
# 	padded_private_msg = private_msg + (padding_character * ((16-len(private_msg)) % 16))
# 	# use the cipher to encrypt the padded message
# 	encrypted_msg = cipher.encrypt(padded_private_msg)
# 	# encode the encrypted msg for storing safely in the database
# 	encoded_encrypted_msg = base64.b64encode(encrypted_msg)
# 	# return encoded encrypted message
# 	return encoded_encrypted_msg

# def decrypt_message(encoded_encrypted_msg, encoded_secret_key, padding_character):
# 	# decode the encoded encrypted message and encoded secret key
# 	secret_key = base64.b64decode(encoded_secret_key)
# 	encrypted_msg = base64.b64decode(encoded_encrypted_msg)
# 	# use the decoded secret key to create a AES cipher
# 	cipher = AES.new(secret_key, AES.MODE_ECB)
# 	# use the cipher to decrypt the encrypted message
# 	decrypted_msg = cipher.decrypt(encrypted_msg)
# 	# unpad the encrypted message
# 	unpadded_private_msg = decrypted_msg.rstrip(padding_character)
# 	# return a decrypted original private message
# 	return unpadded_private_msg


# msg = "hello"
# key = "1234567890123456".encode()
# keyEncoded = base64.b64encode(key)
# encrypted = encrypt_message(msg, keyEncoded, '{')
# print(encrypt)


from cryptidy import symmetric_encryption

# key = symmetric_encryption.generate_key(32)  # 32 bytes == 256 bits
key = "1234567890123456".encode()
some_python_objects = "helloooo my name is"
encrypted = symmetric_encryption.encrypt_message(some_python_objects, key)

print(encrypted)
timestamp, original_object = symmetric_encryption.decrypt_message(encrypted, key)
print(original_object)