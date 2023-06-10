import sys
import logging
import threading
from socket import *
from concurrent.futures import ThreadPoolExecutor

def main():
    nama='client_threadpool'
    logging.warning(f"nama {nama}")    
    
    server_host = '172.16.16.103'
    server_port = 45000
    
    max_threads = threading.active_count() + 1
    
    #jalankan thread sebanyak max_threads+1
    max_threads = 20
    i = 0
    with ThreadPoolExecutor(max_workers = max_threads) as executor:
        while i < max_threads:
            logging.warning(f"thread {i}")
            #max_threads = max_threads+1
            i = i + 1
            executor.submit(run_client, server_host, server_port, i)
         
    
def run_client(server_host, server_port, thread_num): 
    sock = socket(AF_INET, SOCK_STREAM)
    logging.warning("membuka socket")
        
    logging.warning(f"opening socket {server_host, server_port}\r\n")
    sock.connect((server_host, server_port))
        
    # Send data
    logging.warning(f"pesan ke {thread_num}")
    rawmessage = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMN'
    message = 'TIME ' + rawmessage +'\r\n'
    logging.warning(f"sending {message}")
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
