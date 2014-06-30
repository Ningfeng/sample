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
	cmd='iptables -t mangle -I PREROUTING -p tcp --dport 80 -m state --state NEW  -m statistic --mode nth --every 1 --packet 0 -j ACCEPT'
	status=os.popen(cmd,'r').read()
        if status:
            print "error:iptables commands fail!"
            print status
            sys.exit(1)
        else:
            print "iptables commands success!"
	os.popen(cmd,'r').close()


    def extract(self):
	rcmd='iptables-save -c'
	patt=".(\d*).*stat"
        cfd= os.popen(rcmd,'r')
	for line in cfd:
		m=re.match(patt,line)
		if m:
			self.val['syn']=long(m.group(1))
			break
	cfd.close()
		
