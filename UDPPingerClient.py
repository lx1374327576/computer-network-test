from socket import *
import time

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
# message = 'test for ping'
ans = 0
while True:
    start = time.time()
    message = ('Ping %d %s' % (ans+1, start))
    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        print('Sequence %d: Reply from %s      RTT = %.3fs' % (ans+1, serverName, end-start))
    except Exception as e:
        print('Sequence %d: Request timed out' % (ans+1))
    ans += 1
    if ans >= 10:
        break
clientSocket.close()
