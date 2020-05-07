from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
from mininet.node import Node
from mininet.link import TCLink
from cleanup import cleanup

class projectTopo( Mininet ):

    def __init__(self):
        Mininet.__init__(self, link=TCLink, controller=None, cleanup=True)

        #Creating Hosts
        info( "Creating nodes\n" )
        r1 = self.addHost( 'r1', inNamespace=False )
        r2 = self.addHost( 'r2', inNamespace=False )
        r3 = self.addHost( 'r3', inNamespace=False )
        r4 = self.addHost( 'r4', inNamespace=False )
        r5 = self.addHost( 'r5', inNamespace=False )
        r6 = self.addHost( 'r6', inNamespace=False )
        s1 = self.addHost( 's1', inNamespace=False )
        d1 = self.addHost( 'd1', inNamespace=False )
        d2 = self.addHost( 'd2', inNamespace=False )
        d3 = self.addHost( 'd3', inNamespace=False )

        #Establishing the links from hosts to routers
        info( "Creating links\n" )
        self.addLink( s1, r1, intfName2='r1-eth0')
        self.addLink( r1, r2, intfName1='r1-eth1', intfName2='r2-eth0')
        self.addLink( r1, r3, intfName1='r1-eth2', intfName2='r3-eth0')
        self.addLink( r2, r4, intfName1='r2-eth1', intfName2='r4-eth0')
        self.addLink( r3, r4, intfName1='r3-eth1', intfName2='r4-eth1')
        self.addLink( r3, r5, intfName1='r3-eth2', intfName2='r5-eth0')
        self.addLink( r5, r6, intfName1='r5-eth1', intfName2='r6-eth0')
        self.addLink( d1, r4, intfName2='r4-eth2')
        self.addLink( d2, r6, intfName2='r6-eth1')
        self.addLink( d3, r6, intfName2='r6-eth2')

        #Setting interface ip addresses since params1 or params2 just will not work
        source = self.get('s1')
        dest1 = self.get('d1')
        dest2 = self.get('d2')
        dest3 = self.get('d3')
        router1 = self.get('r1')
        router2 = self.get('r2')
        router3 = self.get('r3')
        router4 = self.get('r4')
        router5 = self.get('r5')
        router6 = self.get('r6')
        source.setIP('192.168.1.1/24', intf='s1-eth0')
        dest1.setIP('192.168.2.1/24', intf='d1-eth0')
        dest2.setIP('192.168.3.1/24', intf='d2-eth0')
        dest3.setIP('192.168.4.1/24', intf='d3-eth0')
        router1.setIP('192.168.1.2/24', intf='r1-eth0')
        router1.setIP('10.0.1.0/24', intf='r1-eth1')
        router1.setIP('10.0.2.0/24', intf='r1-eth2')
        router2.setIP('10.0.1.1/24', intf='r2-eth0')
        router2.setIP('10.0.3.1/24', intf='r2-eth1')
        router3.setIP('10.0.4.1/24', intf='r3-eth1')
        router3.setIP('10.0.2.1/24', intf='r3-eth0')
        router4.setIP('10.0.3.2/24', intf='r4-eth0')
        router3.setIP('10.0.5.1/24', intf='r3-eth2')
        router5.setIP('10.0.6.1/24', intf='r5-eth1')
        router4.setIP('10.0.4.2/24', intf='r4-eth1')
        router5.setIP('10.0.5.2/24', intf='r5-eth0')
        router6.setIP('192.168.3.2/24', intf='r6-eth1')
        router6.setIP('10.0.6.2/24', intf='r6-eth0')
        router6.setIP('192.168.4.2/24', intf='r6-eth2')
        router4.setIP('192.168.2.2/24', intf='r4-eth2')


        #Setting default routes for each interface
        s1.cmd( 'ip route add default via 192.168.1.2')
        d1.cmd( 'ip route add default via 192.168.2.2')
        d2.cmd( 'ip route add default via 192.168.3.2')
        d3.cmd( 'ip route add default via 192.168.4.2')
        r1.cmd( 'sysctl net.ipv4.ip_forward=1' )
        r2.cmd( 'sysctl net.ipv4.ip_forward=1' )
        r3.cmd( 'sysctl net.ipv4.ip_forward=1' )
        r4.cmd( 'sysctl net.ipv4.ip_forward=1' )
        r5.cmd( 'sysctl net.ipv4.ip_forward=1' )
        r6.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def start_network(self):
        CLI( self )

if __name__ == '__main__':
    topo = projectTopo()
    topo.start_network()
    cleanup()
