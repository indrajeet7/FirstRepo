from ping import *
from iperf import *

ip_addr='192.168.0.2'
ping_count=10
iperf_port=5201
bandwidth=100*(10**6)


def test_ping():
    print("\nStart ping to test {} for {} times".format(ip_addr, ping_count))
    average_rtt, loss = ping(ip_addr, ping_count)
    status = False

    # Fail condition
    if loss < 30 and average_rtt <= 3:
        status = True

    assert status == True


def test_iperf_tcp():
    print ("\nStart iperf TCP test :: Server={}  Port={}".format(ip_addr, iperf_port))
    mbps=throughput_tcp(ip_addr,iperf_port)
    print("TCP Throughput is :{} Mbps".format(mbps))

    # Fail condition
    assert  mbps>95

'''
def test_iperf_udp():
    print ("\nStart iperf UDP test :: Server={}  Port={} Bandwidth={}".format(ip_addr, iperf_port, bandwidth))
    mbps, loss=throughput_udp(ip_addr,iperf_port,bandwidth)

    print("UDP Throughput is :{} Mbps".format(mbps))
    print("UDP Lost is :{}%".format(loss))

    # Fail condition
    assert mbps>95 and loss<5
'''
