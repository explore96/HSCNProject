import socket
import httplib
import urllib
import os

# Returns The MimeType Of the Given Request File. Mime Type indicates whether file is image or text etc. This is used by the browser
def getMimeType(requesting_file):
    if requesting_file.endswith('jpg'):
        return 'image/jpg'
    else:
        return 'text/html'

# Returns The Content Of The Given File
def getContent(requesting_file):
    requesting_file = requesting_file.lstrip('/')
    if requesting_file == '':
        return html
    else:
        file1 = open(requesting_file,'r')
        return file1.read()


# Main Function In Python
if __name__ == '__main__':

    file1 = open('Main.html','rb')
    html = file1.read()

    os.chdir('/home/tushar/HSCN-Project-master/Files')

    server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8080
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host,port))
    server_sock.listen(5)
    print("Listening For Connection .../")


    while True:
        client_sock, client_addr = server_sock.accept()
        pid = os.fork()
        if(pid == 0):
            print("Got Connection From ", client_addr)
            browser_info = client_sock.recv(1024).decode('utf-8')
            string_list = browser_info.split(' ')
            requesting_file = string_list[1]
            print("Client Requesting File " + requesting_file) 
            mimeType = getMimeType(requesting_file)
            print("mine"+mimeType)
            content = getContent(requesting_file)
            header = "HTTP/1.1 200 OK\n"
            client_sock.send(header.encode('utf-8') + 'Content-Type:' + mimeType + '\n\n' + content)
            client_sock.close()
        else:
            print
