# NetworkProject
How to send to D1

dst = 102 in udplient.py

Sudo python customtopology.py

xterm s1 r1 r3 r4 d1

d1-->python3 udpserver1.py

r4-->python3 udprouter4.py

r3-->python3 udprouter3.py

r1-->python3 udprouter1.py

s1-->python3 udpclient.py
