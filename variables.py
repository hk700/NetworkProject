from nodes import Route

s1 =Route("192.168.1.1",101,8881,None,None)
r1 =Route(("192.168.1.2","10.0.1.0","10.0.2.0"),201,8882,None,None)
r2 =Route(("10.0.1.1","10.0.3.1","10.0.4.1"),202,8883,None, None)
r3 =Route(("10.0.2.1","10.0.3.2","10.0.5.1","10.0.6.1"),203,8884,None,None)
r4 =Route(("10.0.4.2","10.0.7.1"),204,8885,None,None)
r5 =Route(("10.0.5.2","192.168.3.2"),205,8886,None,None)
r6 =Route(("10.0.6.2","192.168.4.2"),206,8887,None,None)
r7 =Route(("10.0.7.2","192.168.2.2"),207,8888,None,None)
d1 =Route("192.168.2.1",102,8889,None,None)
d2 =Route("192.168.3.1",103,8890,None,None)
d3 =Route("192.168.4.1",104,8891,None,None)

'''

hostDic = {101:['192.168.1.1',8880],102:['192.168.2.1',8888],103:['192.168.3.1',8889],104:['192.168.4.1',8890],
           201:[('192.168.1.2','10.0.1.0','10.0.2.0'),8881],202:[('10.0.1.1','10.0.3.1','10.0.4.1'),8882],
           203:[('10.0.2.1','10.0.3.2','10.0.5.1','10.0.6.1'),28883],204:[('10.0.4.2','10.0.7.1'),8884],
           205:[('10.0.5.2','192.168.3.2'),8885],206:[('10.0.6.2','192.168.4.2'),8886],207:[('10.0.7.2','192.168.2.2'),8887)]}

'''
