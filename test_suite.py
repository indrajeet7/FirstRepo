from ping import *
from iperf import *

ip_addr='192.168.78.50'
ping_count=10
iperf_port=5201

def test_ping():
    print("Start ping test to ", ip_addr, ping_count, "times")
    average_rtt, loss = ping(ip_addr, ping_count)
    status = False

    # Fail condition
    if loss < 30 and average_rtt <= 3:
        status = True

    assert status == True


def test_iperf_tcp():
    print ("Start iperf TCP test :: Server=", ip_addr)
    mbps=throughput(ip_addr,iperf_port)
    print("TCP Throughput is :", mbps, "Mbps")

    # Fail condition
    assert  mbps>94

'''
def test_iperf_udp():
    print ("Start iperf UDP test :: Server =", ip_addr)
    mbps=throughput(ip_addr,iperf_port, True)
    print("TCP Throughput is :", mbps, "Mbps")

    # Fail condition
    assert  mbps>95
'''
