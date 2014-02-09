# -*- coding: utf-8 -*-
from socket import *
from datetime import datetime
import sys

def client(numOfPings):
    msg = 'hakloev'
    address = ('Localhost', 12000)
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    print '\033[31m-------------------------UDPPingClient.py--------------------------------'
    print '\033[34mThe message sendt is: ' + msg
    print "\n\033[0m{}\t\t\t\t{}\t\t{}".format('Ping: (msg)', 'seq_num', 'time (ms)')
    print '\033[34m-------------------------------------------------------------------------'

    counter = 0
    while counter <= numOfPings:
        counter += 1
        startTime = datetime.now()
        clientSocket.sendto(msg, address)
        clientSocket.settimeout(1)
        try: 
            recv, addr = clientSocket.recvfrom(1024)
            endTime = datetime.now()
            printRecv(1, recv, counter, (endTime - startTime))
        except timeout:
            endTime = datetime.now()
            printRecv(2, "", counter, (endTime - startTime))
        if counter == numOfPings:
            print '\033[34m-------------------------------------------------------------------------'
            print '\n\033[0mClosing socket'
            clientSocket.close()
            break

def printRecv(typeRecv, recv, counter, et):
    if typeRecv == 1: 
        print "\033[32m Recieved from server: {} \t\t\033[33m| {} |\t\t\033[37m| {} ms\t|".format(recv, str(counter), et.microseconds)
    else:
        print "\033[31m Request timed out. {}\t\t\t\033[33m| {} |\t\t\033[37m| {} ms\t|".format(recv, str(counter), et.microseconds)

if __name__ == '__main__':
    client(int(sys.argv[1]) if len(sys.argv) > 1 else 10)
