import iperf3,json

def throughput(server_ip, port, is_udp=False): 
    client = iperf3.Client()
    client.server_hostname = server_ip
    client.port = port

    key = "sum_received"

    if is_udp == True:
        client.protocol = 'udp'
        key = "sum"
    res = client.run()
    bps = 0

    try:
        j_res = json.loads(str(res))
        bps = j_res["end"][key]["bits_per_second"]/10**6

    except Exception as e:
        print("Could not process", e)

    else:
        return bps

    return None

