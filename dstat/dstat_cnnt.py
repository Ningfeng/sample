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
        self.scale = 0

    def extract(self):
	cnt_file='/proc/sys/net/netfilter/nf_conntrack_count'
	try:
		cnt_fd=dopen(cnt_file)
		for l in cnt_fd:
			self.val['cnnt']=long(l)
		cnt_fd.close()
	except:
		if cnt_fd:
			cnt_fd.close()


# vim:ts=4:sw=4:et
