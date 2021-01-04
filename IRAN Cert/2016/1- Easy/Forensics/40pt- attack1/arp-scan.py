#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scapy.all import * #srp,srp1,Ether,ARP,conf
import sys, getopt, os
import socket
import uuid
from time import sleep 


def get_mac_address(): #get mac 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def usage():
        print "Usage: sudo python ArpScanner.py "

def cutIP(ip):
    #print ip
    iplist = ip.split('.')
    #print iplist
    del iplist[3]
    #print iplist
    ipscan = '.'.join(iplist)
    #print ipscan
    return ipscan
    
from random import randint
def scan(ip):
    sleep(randint(1,4))
    try:
        #ipscan='192.168.1.1/24'
        #print '\nCurrent Network Segment:'+ip
        #ipscan = sys.argv[1] + ".0/24"
        ipscan = cutIP(ip) + ".0/24"
        arpPkt = Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ipscan)
        #arpPkt = Ethernet_head(dst="FF:FF:FF:FF:FF:FF")/ARP_head(pdst=ipscan)
        #print Ethernet_head(dst="FF:FF:FF:FF:FF:FF")
        ans,unans = srp(arpPkt,timeout=2,verbose=False)
        #print ans
    except Exception,e:
        print str(e)
    else:
        for snd,rcv in ans:
            #print ARP.psrc
            list_ip = rcv.sprintf('%ARP.psrc%')
            #print list_ip
            try:
                (hostname, aliaslist, ipaddrlist) = socket.gethostbyaddr(list_ip)
            except:
                hostname = 'Unknow Device'
            list_mac=rcv.sprintf("IP:%ARP.psrc% - MAC:%Ether.src%")
            print list_mac + ' - HostName: '+hostname
    '''
    #return list_mac
    for ipFix in range(1, 254):
        ipscan = "192.168.1."+str(ipFix)
        arpPkt = Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ipscan)
        ans = srp1(arpPkt, timeout = 1, verbose = False)
        if ans:
            print "IP:"+ans.psrc + "    MAC:"+ans.hwsrc
    '''
            
def main(argv):
    if os.geteuid() != 0:
        print "This program must be run as root. Aborting."
        sys.exit()

    # print '\n----Local Network Information----'
    # localIP = socket.gethostbyname(socket.gethostname())
    # print "\nlocal IP: "+localIP
    # ipList = socket.gethostbyname_ex(socket.gethostname())
    # print 'local PC: '+ipList[0]
    mac = get_mac_address()
    print 'local MAC: '+mac +'\n'
    print '----All of active PC in LAN----\n'
    
    
    try:
        opts, args = getopt.getopt(argv, "")
    except getopt.GetoptError:
        usage()

        sys.exit(2)

    #start scan LAN
    scan('192.168.1.6')

   
if __name__ == "__main__":
    main(sys.argv[1:])