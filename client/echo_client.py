#!/usr/bin/python
# Echo client program
import socket
import sys
import argparse

def main():
 parser = argparse.ArgumentParser()
 parser.add_argument('--debug', '-d',action="store_true", help='turn debug on' )
 parser.add_argument('--server', '-s',nargs=1, required=True, help='remote server')
 parser.add_argument('--port', '-p',nargs=1, required=True, help='remote port')
 args = parser.parse_args()
 if args.debug:
   debug = 1

 setup_network(args.server[0],args.port[0])

def setup_network(server,port):
 s = None
 print server,port
 for res in socket.getaddrinfo(server, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
 if s is None:
    print 'could not open socket'
    sys.exit(1)

 send_file(s)

def send_file(s):
 f = open('./ls','r')
 for line in f:
  s.sendall(line)
 f.close()
 s.close()

if __name__ == '__main__':
 main()
