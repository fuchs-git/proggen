import socket

with socket.socket() as web_socket:
    web_socket.connect(('lup', 80))
    web_socket.send(b'GET / HTTP/1.1\r\nHost: lup\r\nConnection: close\r\n\r\n')
    response = b''
    while buffer := web_socket.recv(100):
        response += buffer
    print(response.decode('utf-8'))

