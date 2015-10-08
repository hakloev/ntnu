from socket import *
import ssl
import base64
import getpass

## The code is structured with class-syntax because I wanted to learn Pythons class-syntax ##

class Mail:

    clientSocket = None
    mailServer = None
    serverPort = None
    
    def __init__(self):
        self.clientSocket = ssl.wrap_socket(socket(AF_INET, SOCK_STREAM))
        self.mailServer = 'smtp.gmail.com'
        self.serverPort = 465
    
    def serverInit(self):
        # Create socket called clientSocket and establish a TCP connection with mailserver
        #Fill in start
        self.clientSocket.connect((self.mailServer, self.serverPort))
        #Fill in end

    def destroyServer(self):
        print 'Closing socket'
        self.clientSocket.close()

        print '\n------------------------------------------------'
        print '------------------AND WE ARE DONE---------------'
        print '------------------------------------------------'

    def serverCommunication(self):
        print '------------------------------------------------'
        print '---------------HAKLOEVS MAIL CLIENT-------------'
        print '------------------------------------------------\n'
        
        print 'Using mailserver: ' + self.mailServer
        print 'Using port: ' + str(self.serverPort) + '\n'
        
        uname = raw_input('Username: ')
        pwd = getpass.getpass()

        encodedPw = ("\x00"+ uname + "\x00" + pwd).encode("base64")
        encodedPw = encodedPw.strip("\n")

        toEmail = raw_input('\nMail from: ')
        fromEmail = raw_input('Rcpt to: ')
        realName = raw_input('Realname: ')
        sub = raw_input('Subject: ')
        msg = raw_input('Message: ')
        
        print '\n------------------------------------------------'
        print '------------SENDING MAIL WITH SMTP--------------'
        print '------------PRINTING ALL SERVER RESPONSES-------'
        print '------------------------------------------------\n'

        # Send initial message to server
        recv = self.clientSocket.recv(1024)
        print recv
        if recv[:3] != '220':
            print '220 reply not received from server.'
            
        # Send HELO command and print server response.
        print 'Sending HELO'
        heloCommand = 'HELO Alice' + "\r\n"
        self.clientSocket.send(heloCommand)
        recv1 = self.clientSocket.recv(1024)
        print recv1
        if recv1[:3] != '250':
            print '250 reply not received from server.'

        # Send AUTH comand and print server response
        print 'Sending AUTH'
        self.clientSocket.send("AUTH PLAIN " + encodedPw + "\r\n")
        recv2 = self.clientSocket.recv(1024)
        print recv2
        if recv2[:3] != '235':
            print '235 reply not received from server.'

        # Send HELO after AUTH
        print 'Sending HELO again'
        heloCommand = 'HELO smtp.google.com' + "\r\n"
        self.clientSocket.send(heloCommand)
        recv4 = self.clientSocket.recv(1024)
        print recv4
        if recv4[:3] != '250':
            print '250 reply not received from server.'

        # Send MAIL FROM command and print server response.
        # Fill in start
        print 'Sending MAIL FROM'
        self.clientSocket.send('MAIL FROM: <' + toEmail + '>' + "\r\n")
        recv5 = self.clientSocket.recv(1024)
        print recv5
        if recv5[:3] != '250':
            print '250 reply not received from server.'
        # Fill in end

        # Send RCPT TO command and print server response.
        # Fill in start
        print 'Sending RCPT TO'
        self.clientSocket.send('RCPT TO: <' + fromEmail + '>' + "\r\n")
        recv6 = self.clientSocket.recv(1024)
        print recv6
        if recv6[:3] != '250':
            print '250 reply not received from server.'
        # Fill in end

        # Send DATA command and print server response.
        # Fill in start
        print 'Sending DATA'
        self.clientSocket.send('DATA' + "\r\n")
        recv7 = self.clientSocket.recv(1024)
        print recv7
        if recv7[:3] != '354':
            print '354 reply not received from server.'
        # Fill in end

        #########################################################
        ##############     THE MESSAGE ITSELF    ################
        #########################################################

        print '------------------------------------------------'
        print '--------------SENDING MESSAGE ITSELF------------'
        print '------------------------------------------------\n'

        self.clientSocket.send('To: ' + fromEmail + "\r\n")
        self.clientSocket.send('From: ' + realName +  ' <' + toEmail + '>' + "\r\n")

        # Send message data.
        # Fill in start
        print 'Sending MESSAGE'
        self.clientSocket.send('Content-Type: text/plain\r\n')
        self.clientSocket.send('Subject: ' + sub.strip() + "\r\n")
        self.clientSocket.send("\r\n")
        self.clientSocket.send(msg.strip() + "\r\n")
        # Fill in end
        
        # Send endmessage
        # Fill in start
        self.clientSocket.send("\r\n.\r\n")
        recv6 = self.clientSocket.recv(1024)
        print recv6
        if recv6[:3] != '250':
            print '250 reply not received from server.'
        # Fill in end
        
        # Send QUIT command and get server response.
        # Fill in start
        print 'Sending QUIT'
        self.clientSocket.send('QUIT' + "\r\n")
        recv8 = self.clientSocket.recv(1024)
        print recv8
        if recv8[:3] != '221':
            print '221 reply not received from server.'
        # Fill in end

## BUILD UP AND TEARDOWN ##
client = Mail()
client.serverInit()
client.serverCommunication()
client.destroyServer()
###########################
