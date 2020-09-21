# Very Basic Honeypot v1

As its name says, it is a very simple trap to capture possible scanners. <br>
The VBH opens a socket (TCP or UDP) and waits for connections. <br>
If receive at least 1 packet, it will log into a file (Monitor Mode) or log into a file and create a firewall rule (Agressive Mode). <br>

## Dependencies:

* Python3.x +
* iptables (Only for aggressive mode)
* datetime python package (pip3 install datetime) <br>

## Configuring
All your configurations should be set up on file config_vbh.py <br>
Keep both files (vbh.py and config_vbh.py) in the same directory to work properly. <br>

## Running
$ sudo python3 vbh.py &<br>

## Stopping
root@laptop-leandro:/tmp# ps aux | grep vbh.py <br>
root     16792  0.0  0.2  14352  9368 pts/3    S    18:35   0:00 python3 vbh.py <br>
root     17198  0.0  0.0   6076   880 pts/3    S+   18:36   0:00 grep vbh.py <br>
root@laptop-leandro:/tmp# kill -9 16792 <br>
root@laptop-leandro:/tmp#  <br>


