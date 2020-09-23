"""
VBH v1
https://github.com/bacherol/vbh
leandrobachero@gmail.com
Sep/2020

Configuration File to use with VBH v1
"""

## host
# Set an IP which belongs to your machine to listen on
# Default: host = '0.0.0.0'
host = '0.0.0.0'
## port
# Set an Port to listen on
# Default = port '8080'
port = 8080
## proto
# You can choose to listen on TCP or UDP
# Default: proto = 'tcp'
proto = 'tcp'
## mode
# You can choose between monitor or aggressive
# monitor = Just monitor the scans and log into a file (/var/log/vbh.log)
# aggressive = Monitor mode + add firewall rules to your iptables (Chain INPUT)
# Default: mode = 'monitor'
mode = 'monitor'
## logfile
# File to log all entries
# Default: /var/log/vbh.log
logfile = '/var/log/vbh.log'
