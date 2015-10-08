#import socket module
from socket import *
import socket as sock

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket

#Fill in start
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection 
    print 'Ready to serve on port ' + str(serverPort)
    connectionSocket, addr =  serverSocket.accept()   
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        f.close()
        #Send one HTTP header line into socket
        #Fill in start
        print 'Sending HTTP Header'
        connectionSocket.send('HTTP/1.0 200 OK\r\n')
        connectionSocket.send("Content-Type: text/html\r\n\r\n")
        #Fill in end
        
        #Send the content of the requested file to the client
        print 'Sending HTML-file: ' + filename
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        print 'Closing client socket\n'
    except IOError:
        #Send response message for file not found
        #Fill in start
        print 'Exception: IOError'
        print 'Tried HTML: ' + filename
        print 'Sending 404.html'
        try:
            e = open('404.html')
            errorMessage = e.readlines()
            e.close()
            for i in range(0, len(errorMessage)):
                connectionSocket.send(errorMessage[i])
        #Fill in end
        
            #Close client socket
            #Fill in start
            connectionSocket.close()
            print 'Closing client socket'
            #Fill in end
        except sock.error:
            print 'Broken pipe, must create new socket'
            pass
        print 

serverSocket.close()
