import iperf3

def throughput_tcp(server_ip, port, duration=10):
    client = iperf3.Client()
    client.server_hostname = server_ip
    client.port = port
    client.duration=duration

    response=client.run()
    mbps=response.sent_Mbps

    return mbps


def throughput_udp(server_ip, port, bandwidth, duration=10):
    client = iperf3.Client()
    client.server_hostname = server_ip
    client.port = port
    client.duration=duration

    client.protocol = 'udp'
    client.bandwidth = bandwidth

    response=client.run()
    mbps=response.Mbps
    loss=response.lost_percent
    return mbps, loss



