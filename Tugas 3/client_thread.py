import sys
import logging
import threading
from socket import *

def main():
    nama='client_thread'
    logging.warning(f"nama {nama}")    
    
    server_host = '172.16.16.103'
    server_port = 45000
    
    #max_threads = threading.active_count() + 1
    max_threads = threading.active_count() + 1
    
    #jalankan thread sebanyak max_threads+1
    #for i in range(max_threads+1):
    max_threads = 1
    i = 0
    while i < max_threads:
        i = i + 1
        max_threads = i + 1
        logging.warning(f"thread {i}")
        client_thread = ClientThread(server_host, server_port)
        client_thread.start()
                
    for thread in threading.enumerate():
        if thread != threading.main_thread():
            thread.join() 
    
class ClientThread(threading.Thread):  
    def __init__(self, server_host, server_port):
        threading.Thread.__init__(self)
        self.server_host = server_host
        self.server_port = server_port
                                  
    def run(self):
        sock = socket(AF_INET, SOCK_STREAM)
        logging.warning("membuka socket")
        
        logging.warning(f"opening socket {self.server_host, self.server_port}\r\n")
        sock.connect((self.server_host, self.server_port))
        
        # Send data
        rawmessage = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
        message = 'TIME ' + rawmessage + '\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode('UTF-8'))
        
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        #while amount_received < amount_expected:
        data = sock.recv(1024).decode('UTF-8')
        amount_received += len(data)
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
        
        logging.warning("closing")
        sock.close()

if __name__=='__main__':
    #for i in range(1,3):
    main()
