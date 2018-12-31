from ping import *

ip_addr='192.168.78.50'
ping_count=10


def test_ping_func():
    average_rtt, loss = ping(ip_addr, ping_count)
    status = False

    # Fail condition
    if loss < 30 and average_rtt <= 5:
        status = True

    assert status == True
