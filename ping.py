from multiping import MultiPing
import time,sys

def ping(ip_addr,iterations):
    total_rtt=0
    average_rtt=0
    no_responses_cnt=0
    rtt_list=[]


    for i in range(iterations):
        time.sleep(0.2)
        mp = MultiPing([ip_addr])
        mp.send()
        responses, no_responses = mp.receive(1)

        for _, rtt in responses.items():
            #print("{} responded in {} seconds".format(addr, rtt))
            rtt_list.append(rtt)
            total_rtt+=rtt

        if no_responses:
            print ("These address did not respond: {}".format(no_responses))
            no_responses_cnt+=1

        
    average_rtt=(total_rtt/iterations)*1000
    loss = (no_responses_cnt/iterations)*100

    print("Average Round-trip time is {} ms".format(average_rtt))
    print("Loss is {}%".format(loss))

    return average_rtt, loss
