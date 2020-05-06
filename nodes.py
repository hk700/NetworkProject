
class Route:

    def __init__(self, ip, id, port,nexthop,dst):
        self.id = str(id)
        self.ip = str(ip)
        self.port = port
        self.nexthop =nexthop
        self.dst = dst
