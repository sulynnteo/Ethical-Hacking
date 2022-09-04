Note:
    - You'll need gnupg version 2.4.0 or higher to run, as there is argument added in newest version to work
    - Ensure that gnupg is installed on both Attacker and Victim's machine
    - Ensure ransom.py is on both machine ^

Steps on running:
    1. Run cmd and enter in terminal:
        - python3 ransom.py

    2. Attacker enter encrypted key in input

    3. After entering:
        - important.txt will be encrypted into encrypted_message.asc
        - userinput stored into key.txt and encrypted into encrypted_key.asc
        - important.txt and key.txt will be removed
        - threaten message will be displayed in print form
    
    4. Decryption (optional):
        - run python3 decrypt.py
        - encrypted_message.asc and encrypted_key.asc will be used to decrypt the message
        - message is saved as important.txt
