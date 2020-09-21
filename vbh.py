"""
VBH v1
https://github.com/bacherol/vbh
leandrobachero@gmail.com
Sep/2020

DO NOT CHANGE THIS FILE! Unless you have enough knowledge to do it.
Change config_vbh.py to set your configuration!
"""

from config_vbh import *
from datetime import datetime
from os import system
import socket

# Basic check
if type(port) != int:
    exit('Port must be an integer!')
if proto.lower() != 'tcp' and proto.lower() != 'udp':
    exit('Protocol must be TCP or UDP!')

# Mode Monitor
if mode.lower() == 'monitor':
    if proto.lower() == 'tcp':
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (host, int(port))
        try:
            tcp.bind(orig)
        except:
            exit(f'Could not open a new socket using {host}:{port}. Check if the IP is correct and/or the port is not being used.')
        tcp.listen(1)
        while True:
            con, client = tcp.accept()
            with open(logfile, 'a') as arquivo:
                arquivo.write(f'{datetime.now()} - Detected TCP connection from {client[0]} on port {port}\n')
            con.close()
    elif proto.lower() == 'udp':
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (host, port)
        try:
            udp.bind(orig)
        except:
            exit(f'Could not open a new socket using {host}:{port}. Check if the IP is correct and/or the port is not being used.')
        while True:
            con, client = udp.recvfrom(1024)
            with open(logfile, 'a') as arquivo:
                arquivo.write(f'{datetime.now()} - Detected UDP connection from {client[0]} on port {port}\n')

# Mode Aggressive
elif mode.lower() == 'aggressive':
    if proto.lower() == 'tcp':
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (host, port)
        try:
            tcp.bind(orig)
        except:
            exit(f'Could not open a new socket using {host}:{port}. Check if the IP is correct and/or the port is not being used.')
        tcp.listen(1)
        while True:
            con, client = tcp.accept()
            with open(logfile, 'a') as arquivo:
                arquivo.write(f'{datetime.now()} - Detected TCP conection from {client[0]} on port {port}\n')
                rule_check = system(f'iptables -C INPUT -s {client[0]} -p tcp --dport {port} -m comment --comment "Bachero" -j DROP > /dev/null 2>&1')
                if rule_check != 0:
                    system(f'iptables -I INPUT -s {client[0]} -p tcp --dport {port} -m comment --comment "Bachero" -j DROP')
                    arquivo.write(f'{datetime.now()} - Firewall rule added to chain INPUT to IP {client[0]}.\n')
                else:
                    arquivo.write(f'{datetime.now()} - {client[0]} already added to chain INPUT and still receiving packets on socket. Check your firewall!\n')
            con.close()
    elif proto.lower() == 'udp':
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (host, port)
        try:
            udp.bind(orig)
        except:
            exit(f'Could not open a new socket using {host}:{port}. Check if the IP is correct and/or the port is not being used.')
        while True:
            con, client = udp.recvfrom(1024)
            with open(logfile, 'a') as arquivo:
                arquivo.write(f'{datetime.now()} - Detected UDP connection from {client[0]} on port {port}\n')
                rule_check = system(f'iptables -C INPUT -s {client[0]} -p udp --dport {port} -m comment --comment "Bachero" -j DROP > /dev/null 2>&1')
                if rule_check != 0:
                    system(f'iptables -I INPUT -s {client[0]} -p udp --dport {port} -m comment --comment "Bachero" -j DROP')
                    arquivo.write(f'{datetime.now()} - Firewall rule added to chain INPUT to IP {client[0]}.\n')
                else:
                    arquivo.write(f'{datetime.now()} - {client[0]} already added to chain INPUT and still receiving packets on socket. Check your firewall!\n')


