import sys
import socket
import logging
import threading


def kirim_data(kosong):
    nama='client_2'
    logging.warning(f"nama {nama}")    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.103', 45000)
    logging.warning(f"opening socket {server_address}\r\n")
    sock.connect(server_address)

    try:
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
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    threads = []
    for i in range(3):
        t = threading.Thread(target=kirim_data, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()
