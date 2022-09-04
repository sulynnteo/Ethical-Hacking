## optional Decryption
#!/usr/bin/env python3
import sys, gnupg, os

homedir = "/home/kali/Desktop/.gnupg"
gpg = gnupg.GPG(homedir)

## decrypt file and import keys over
with open('encrypted_key.asc', 'rb') as f:
    key_data = open('encrypted_key.asc').read()
    import_result = gpg.import_keys(key_data)

    gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')

    key = gpg.list_keys()
    with open('encrypted_message.asc','rb')as k:
        status = gpg.decrypt_file(k, passphrase = key , output = "important.txt")

print(status.ok)
print(status.stderr)
