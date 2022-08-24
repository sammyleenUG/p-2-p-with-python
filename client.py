from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint
 
class Client(DatagramProtocol):
    def __init__(self,host,port):
        if host == 'localhost':
            host = '127.0.0.1'
        
        self.port = port
        self.address = None
        self.server = '127.0.0.1', 9999
        print('Client working on port : ',self.port)
    
    def startProtocol(self):
        self.transport.write('ready'.encode('utf-8'), self.server)

    def datagramReceived(self,datagram,addr):
        if not self.address:
            print("choose client from: ", datagram)
            self.address = input("Address="), int(input("Port="))
            reactor.callInThread(self.send_message)
        print(addr,":",datagram)

    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)
    
if __name__ == '__main__':
    port = randint(1000,5000)
    reactor.listenUDP(port, Client('localhost',port))
    reactor.run()