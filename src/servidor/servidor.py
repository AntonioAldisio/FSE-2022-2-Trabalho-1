# #!/usr/bin/env python3
import json
import socket
from utils.save_json import save_json

def initSocket(ip, port, diretorio):
    dir = 'src/json/'+diretorio+'.json'
    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.bind((ip, port))
        tcp.listen(2)
        while True:
            con, cliente = tcp.accept()
            print ('Concetado por', cliente)
            while True:
                received = json.loads(tcp.recv(8192).decode("utf-8"))
                save_json(dir)
    except KeyboardInterrupt:
        sys.exit(0)
