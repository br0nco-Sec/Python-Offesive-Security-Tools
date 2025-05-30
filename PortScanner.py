import sys
import socket
import argparse

#### Port Scanner and Banner grabber created by Br0nco

def banner_grabber(host, port):
    port = int(port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(2)
            s.connect((host,port))
            response = s.recv(1024)
            print(f"[+] Response from HOST {host}:{port} ->\n{response.decode}")
        except Exception as e:
            print(f"Error while trying to connect to {port}- {e}")

def port_scanner(host):
    ports = [21,22,23,25,53,80,110,143,443,445,993,995,3306,3389,8080]

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"\n[+] Port {port} OPEN on HOST {host}")
        except Exception as e:
            print("Error while trying to connect to port {ports}- {e}")




if __name__=="__main__":
    global_parser = argparse.ArgumentParser(description='Port scanner tool and banner grab')
    subparsers = global_parser.add_subparsers(dest='command', title='Commands', required=True)

    # Banner grabber
    banner_parser = subparsers.add_parser('Banner', help='Grab the banner of a port.')
    banner_parser.add_argument('--host', required=True, help='--host 10.10.10.10')
    banner_parser.add_argument('--port',required=True, help='--port 22')

    # port Scanner
    portscan_parser = subparsers.add_parser('Portscan', help='Scan ports from host')
    portscan_parser.add_argument('--host', required=True, help='--host 10.10.10.10')
    
    args = global_parser.parse_args()

    if args.command == 'Banner':
        banner_grabber(args.host, args.port)
    elif args.command == 'Portscan':
        port_scanner(args.host)
