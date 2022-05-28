#!/usr/bin/env python

import os
import time
import subprocess
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info


class CustomTopo (Topo):

    def build(self):
        # Switches
    	self.s1 = self.addSwitch( 's1' )
    	self.s2 = self.addSwitch( 's2' )
        # Hosts
    	self.h1 = self.addHost( 'h1', ip='10.0.0.1' )
    	self.h2 = self.addHost( 'h2', ip='10.0.0.2' )
    	self.h3 = self.addHost( 'h3', ip='10.0.0.3' )
    	self.h4 = self.addHost( 'h4', ip='10.0.0.4' )
        self.h5 = self.addHost( 'h5', ip='10.0.0.5' )
    	self.h6 = self.addHost( 'h6', ip='10.0.0.6' )
    	self.h7 = self.addHost( 'h7', ip='10.0.0.7' )
    	self.h8 = self.addHost( 'h8', ip='10.0.0.8' )
        self.h9 = self.addHost( 'h9', ip='10.0.0.9' )
    	self.h10 = self.addHost( 'h10', ip='10.0.0.10' )
    	self.h11 = self.addHost( 'h11', ip='10.0.0.11' )
    	self.h12 = self.addHost( 'h12', ip='10.0.0.12' )
        self.h13 = self.addHost( 'h13', ip='10.0.0.13' )
    	self.h14 = self.addHost( 'h14', ip='10.0.0.14' )
    	self.h15 = self.addHost( 'h15', ip='10.0.0.15' )
    	self.h16 = self.addHost( 'h16', ip='10.0.0.16' )
        self.h17 = self.addHost( 'h17', ip='10.0.0.17' )
    	self.h18 = self.addHost( 'h18', ip='10.0.0.18' )
    	self.h19 = self.addHost( 'h19', ip='10.0.0.19' )
    	self.h20 = self.addHost( 'h20', ip='10.0.0.20' )
        self.h21 = self.addHost( 'h21', ip='10.0.0.21' )
    	self.h22 = self.addHost( 'h22', ip='10.0.0.22' )
    	self.h23 = self.addHost( 'h23', ip='10.0.0.23' )
    	self.h24 = self.addHost( 'h24', ip='10.0.0.24' )
        self.h25 = self.addHost( 'h25', ip='10.0.0.25' )
    	self.h26 = self.addHost( 'h26', ip='10.0.0.26' )
    	self.h27 = self.addHost( 'h27', ip='10.0.0.27' )
    	self.h28 = self.addHost( 'h28', ip='10.0.0.28' )
        self.h29 = self.addHost( 'h29', ip='10.0.0.29' )
    	self.h30 = self.addHost( 'h30', ip='10.0.0.30' )
    	self.h31 = self.addHost( 'h31', ip='10.0.0.31' )
    	self.h32 = self.addHost( 'h32', ip='10.0.0.32' )
        self.hUDP = self.addHost( 'hUDP', ip='10.0.0.50' )
        # sinks
        self.sinkUDP = self.addHost( 'sinkUDP', ip='10.0.0.100' )
        self.sinkTCP1 = self.addHost( 'sinkTCP1', ip='10.0.0.201' )
    	self.sinkTCP2 = self.addHost( 'sinkTCP2', ip='10.0.0.202' )
    	self.sinkTCP3 = self.addHost( 'sinkTCP3', ip='10.0.0.203' )
    	self.sinkTCP4 = self.addHost( 'sinkTCP4', ip='10.0.0.204' )
        self.sinkTCP5 = self.addHost( 'sinkTCP5', ip='10.0.0.205' )
    	self.sinkTCP6 = self.addHost( 'sinkTCP6', ip='10.0.0.206' )
    	self.sinkTCP7 = self.addHost( 'sinkTCP7', ip='10.0.0.207' )
    	self.sinkTCP8 = self.addHost( 'sinkTCP8', ip='10.0.0.208' )
        self.sinkTCP9 = self.addHost( 'sinkTCP9', ip='10.0.0.209' )
    	self.sinkTCP10 = self.addHost( 'sinkTCP10', ip='10.0.0.210' )
    	self.sinkTCP11 = self.addHost( 'sinkTCP11', ip='10.0.0.211' )
    	self.sinkTCP12 = self.addHost( 'sinkTCP12', ip='10.0.0.212' )
        self.sinkTCP13 = self.addHost( 'sinkTCP13', ip='10.0.0.213' )
    	self.sinkTCP14 = self.addHost( 'sinkTCP14', ip='10.0.0.214' )
    	self.sinkTCP15 = self.addHost( 'sinkTCP15', ip='10.0.0.215' )
    	self.sinkTCP16 = self.addHost( 'sinkTCP16', ip='10.0.0.216' )
        self.sinkTCP17 = self.addHost( 'sinkTCP17', ip='10.0.0.217' )
    	self.sinkTCP18 = self.addHost( 'sinkTCP18', ip='10.0.0.218' )
    	self.sinkTCP19 = self.addHost( 'sinkTCP19', ip='10.0.0.219' )
    	self.sinkTCP20 = self.addHost( 'sinkTCP20', ip='10.0.0.220' )
        self.sinkTCP21 = self.addHost( 'sinkTCP21', ip='10.0.0.221' )
    	self.sinkTCP22 = self.addHost( 'sinkTCP22', ip='10.0.0.222' )
    	self.sinkTCP23 = self.addHost( 'sinkTCP23', ip='10.0.0.223' )
    	self.sinkTCP24 = self.addHost( 'sinkTCP24', ip='10.0.0.224' )
        self.sinkTCP25 = self.addHost( 'sinkTCP25', ip='10.0.0.225' )
    	self.sinkTCP26 = self.addHost( 'sinkTCP26', ip='10.0.0.226' )
    	self.sinkTCP27 = self.addHost( 'sinkTCP27', ip='10.0.0.227' )
    	self.sinkTCP28 = self.addHost( 'sinkTCP28', ip='10.0.0.228' )
        self.sinkTCP29 = self.addHost( 'sinkTCP29', ip='10.0.0.229' )
    	self.sinkTCP30 = self.addHost( 'sinkTCP30', ip='10.0.0.230' )
    	self.sinkTCP31 = self.addHost( 'sinkTCP31', ip='10.0.0.231' )
    	self.sinkTCP32 = self.addHost( 'sinkTCP32', ip='10.0.0.232' )
        # Links
        # S1 to S2
    	self.addLink( self.s1, self.s2)
        # Hosts 1..33 to S1
        for self.host in self.hosts():
            if (str(self.host)[0] == 's'):
                self.addLink( self.host, self.s2 )
            else:
                self.addLink( self.host, self.s1 )



def CHOKeNet():

    """Create an empty network and add nodes to it."""
    os.system("sudo mn -c")
    topo = CustomTopo()
    net = Mininet(topo)
    net.start()


    info('*** Adding bandwidth of 10mbit to all links\n')
    for i in range(2,35):
        os.system("sudo tc qdisc add dev s1-eth" + str(i) + " root netem rate 10mbit delay 1ms")
        os.system("sudo tc qdisc add dev s2-eth" + str(i) + " root netem rate 10mbit delay 1ms")

    info('*** configuring choke between switches\n')
    os.system("sudo tc qdisc add dev s2-eth1 root netem rate 1gbit delay 1ms")  # incoming traffic
    # outgoing traffic -> choke
    os.system("sudo tc qdisc add dev s1-eth1 root handle 1: tbf rate 1mbit burst 50000 limit 524288 ")
    os.system("sudo tc qdisc add dev s1-eth1 parent 1: handle 2: choke limit 65536 max 32768 min 4096 burst 4097 avpkt 1000 bandwidth 1mbit probability 0.5")  #choke config
    #os.system("sudo tc qdisc add dev s1-eth1 parent 1: handle 2: red limit 524288 max 262144 min 32768 burst 64 avpkt 1000 bandwidth 1mbit probability 0.5")   #red config for comparison

    info('*** Launching Wireshark on bottleneck link\n')
    net.get('s1').cmd('wireshark &')

    raw_input("Press Enter to start tcp&udp streams...")

    info('*** Launching iPerf3 in server mode on sinkTCP1..32 and sinkUDP\n')
    for net.host in net.hosts:
        if(str(net.host)[0] == 's'):
            info('*** ' + str(net.host) + " : " + "iperf3 -s &\n")  #print the cmd
            net.host.cmd('iperf3 -s &')

    info('*** Launching iPerf3 in UDP client mode on host hUDP\n')
    info('*** ' + str(net.get('hUDP')) + " : " + "iperf3 -u -c 10.0.0.100 -t 180 -b 2mbit -l 1kbit &\n")    #print the cmd
    net.get('hUDP').cmd('iperf3 -u -c 10.0.0.100 -t 180 -b 2mbit -l 1kbit &')

    
    info('*** Launching iPerf3 in TCP client mode on host h1..32\n')
    for net.host in net.hosts:
        if(not(str(net.host)[0] == 's' or net.host == net.get('hUDP'))):
            time.sleep(0.25)
            info('*** ' + str(net.host) + " : " + 'iperf3 -c 10.0.0.'  + str(200 + int(str(net.host)[1:3])) + ' -t 180  &\n')   #print the cmd
            net.host.cmd('iperf3 -c 10.0.0.' +str(200 + int(str(net.host)[1:3])) + ' -t 180  &')
    
    
    info('*** Running CLI\n' )
    CLI(net)

    info('*** Stopping network' )
    net.stop()
    

if __name__ == '__main__':
    setLogLevel('info')
    CHOKeNet()
