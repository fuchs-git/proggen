import socket

with socket.socket() as server_socket:
    server_socket.bind(('', 8080))
    server_socket.listen()

    anzahl = 0
    while True:
        s= r'''<br>Hello World'''
        anzahl += 1
        client, info = server_socket.accept()
        print(anzahl, client, info)
        client.send( b'HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hello '
                     + str(info).encode('utf-8') + s.encode('utf-8')
                     + b'</h1></body></html>')
        req = client.recv(1024)
        client.send( req)
        print(req.decode('utf-8'))
        # client.send(f'HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hello {str(info)}</h1></body></html>'.encode('utf-8'))

