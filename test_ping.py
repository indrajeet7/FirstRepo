from practice_multiping import *

ip_addr=input("Enter IP Address.......")
iteration=int(input("Enter number of iterations....."))


def test_ping_func():
    assert ping_func(ip_addr,iteration)==True


