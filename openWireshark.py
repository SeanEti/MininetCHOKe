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
        # Links
        # Hosts 1&2 to S1
    	self.addLink( self.h1, self.s1 )
    	self.addLink( self.h2, self.s1 )
    	# S1 to S2
    	self.addLink( self.s1, self.s2 )
    	# Hosts 3&4 to S2
    	self.addLink( self.h3, self.s2 )
    	self.addLink( self.h4, self.s2 )


def CHOKeNet():

    """Create an empty network and add nodes to it."""
    os.system("sudo mn -c")
    topo = CustomTopo()
    net = Mininet(topo, waitConnected=True )
    net.start()
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    info('*** Adding delay of 20ms to all links\n')
    os.system("sudo tc qdisc add dev s1-eth1 root netem delay 20ms")
    os.system("sudo tc qdisc add dev s1-eth2 root netem delay 20ms")
    os.system("sudo tc qdisc add dev s1-eth3 root netem delay 20ms")
    os.system("sudo tc qdisc add dev s2-eth1 root netem delay 20ms")
    os.system("sudo tc qdisc add dev s2-eth2 root netem delay 20ms")
    os.system("sudo tc qdisc add dev s2-eth3 root netem delay 20ms")

    info('*** Launching Wireshark on all hosts\n')
    h1.cmd('wireshark &')
    h2.cmd('wireshark &')
    h3.cmd('wireshark &')
    h4.cmd('wireshark &')

    raw_input("Press Enter to start tcp&udp streams...")

    info('*** Launching iPerf3 in TCP server mode on host h3\n')
    h3.cmd('iperf3 -s &')

    info('*** Launching iPerf3 in UDP server mode on host h4\n')
    h4.cmd('iperf3 -s -u &')

    info('*** Launching iPerf3 in TCP client mode on host h1\n')
    h1.cmd("iperf3 -c 10.0.0.3 -t 60 -J > TCP.json &")

    info('*** Launching iPerf3 in UDP client mode on host h2\n')
    h2.cmd("iperf3 -u -c 10.0.0.4 -t 60 -J > UDP.json &")
    
    info('*** Running iPerf3 - 60 seconds...\n')
    time.sleep(60)
    
    info('*** Running CLI\n' )
    CLI(net)

    info('*** Stopping network' )
    net.stop()
    

if __name__ == '__main__':
    setLogLevel('info')
    CHOKeNet()
