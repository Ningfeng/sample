### Author: zhoujz<zhoujz@chinanetcenter.com>
class dstat_plugin(dstat):
    def __init__(self):
        self.name = 'system'
        self.timefmt = '%s'
        self.type = 's'

        self.width = len(time.strftime(self.timefmt, time.localtime()))
        self.scale = 0
        self.vars = ('time',)

        
    def extract(self):
        self.val['time'] = time.strftime(self.timefmt, time.localtime(starttime))

