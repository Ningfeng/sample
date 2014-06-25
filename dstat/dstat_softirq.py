### Author: zhoujz<zhoujz@chinanetcenter.com>

class dstat_plugin(dstat):
    def __init__(self):
        self.name = 'softirq'
        self.vars = ('hi','timer','net_tx', 'net_rx', 'bio_poll', 'tasklet','sched', 'hrtimer', 'rcu')
        self.timefmt = '%s'
        self.type = 'd'
        self.width = 10
        self.scale = 1000
        self.open('/proc/stat')
    
    def extract(self):
        for l in self.splitlines():
            if len(l) < 3: continue
            name = l[0]
            if name != 'softirq': continue
            self.set2['hi'] = long(l[2])
            self.set2['timer'] = long(l[3])
            self.set2['net_tx'] = long(l[4])
            self.set2['net_rx'] = long(l[5])
            self.set2['bio_poll'] = long(l[6])
            self.set2['tasklet'] = long(l[7])
            self.set2['sched'] = long(l[8])
            self.set2['hrtimer'] = long(l[9])
            self.set2['rcu'] = long(l[10])
            break
        
        #self.set2['time'] = time.strftime(self.timefmt, time.localtime(starttime))
        for name in self.vars:
            self.val[name] = self.set2[name] * 1.0 

#   def check(self):
