#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_argument():
    parser=argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="the target ip /ip range",required=True)
    option=parser.parse_args()
    return option

def scan(ip) :
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list,unanswered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)
    clients_list = []
    for element in answered_list:
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(client_dict)
    return  clients_list

def print_result(results):
    print("IP\t\t\tMAC\n----------------------------------------------")
    for result in results:
        print(result["ip"]+"\t\t"+result["mac"])



# scan("192.168.88.1/24")

option=get_argument()
result=scan(option.target)
print_result(result)