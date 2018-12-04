#!/usr/bin/env python
# coding: utf-8



from mininet.topo import Topo
#Add Hosts and Switches

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
    #Add Links
        self.addLink(h1,s1)
        self.addLink(s1,s2)
        self.addLink(s2,s5)
        self.addLink(s3,s4)
        self.addLink(s4,s2)
        self.addLink(s5,s4)
        self.addLink(s1,s3)
        self.addLink(s3,s5)
        self.addLink(s4,h2)
topos = {'mytopo':(lambda:MyTopo())}

