### Author: zhoujz<zhoujz@chinanetcenter.com>

import  commands
class dstat_plugin(dstat):
    """
    Total Number of netfliter connect on this system.
    """
    def __init__(self):
        self.name = 'syn-num'
        self.vars = ('syn',)
        self.type = 'd'
        self.width = 10 
        self.scale = 0
        status=commands.getoutput('sudo iptables -t mangle -I PREROUTING -p tcp --dport 80 -m state --state NEW  -m statistic --mode nth --every 1 --packet 0 -j ACCEPT')
        if status:
            print "error:iptables commands fail!"
            print status
            sys.exit(1)
        else:
            print "iptables commands success!"

    def extract(self):
        syn= os.popen('cat /proc/sys/net/ipv4/ipfrag_time').read();
        self.val['syn']=long(syn)
