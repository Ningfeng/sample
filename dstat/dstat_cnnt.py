### Author: zhoujz<zhoujz@chinanetcenter.com>

class dstat_plugin(dstat):
    """
    Total Number of netfliter connect on this system.
    """
    def __init__(self):
        self.name = 'cnnt'
        self.vars = ('cnnt',)
        self.type = 'd'
        self.width = 10 
        #self.scale = 100
        self.open('/proc/sys/net/netfilter/nf_conntrack_count')

    def extract(self):
        for l in self.splitlines():
            if len(l) < 1: continue
            self.val['cnnt'] = long(l[0]) * 1.0


# vim:ts=4:sw=4:et
