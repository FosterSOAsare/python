import socket

def scan(targets , port) : 
   for target in targets : 
    print('Scanning target' , target)
    for i in range( 0 , port):
        scan_target(target , i)

def scan_target (ip , port) : 
    try : 
        sock = socket.socket()
        sock.connect((ip , port))
        print('[+] Port is open' , port )
        sock.close()
    except : 
      pass

scan(['172.20.10.4' , '172.20.10.2'] , 100)