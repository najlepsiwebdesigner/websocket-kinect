import pylzma, pprint
from twisted.internet import reactor
from autobahn.websocket import WebSocketClientFactory, \
                               WebSocketClientProtocol, \
                               connectWS
 
 


class EchoClientProtocol(WebSocketClientProtocol):
 

   # def sendHello(self):
      # self.sendMessage("Hello, world!")
 
   def onOpen(self):
      # self.sendHello()
      print "Connected!"
 

       

   def onMessage(self, msg, binary):
      # decompressed = pylzma.decompress(msg)
      print "message!";
      
 
 
if __name__ == '__main__':
 
   factory = WebSocketClientFactory("ws://localhost:8888", debug = False)
   factory.protocol = EchoClientProtocol
   connectWS(factory)
   reactor.run()