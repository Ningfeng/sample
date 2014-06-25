### Author: zhoujz<zhoujz@chinanetcenter.com>
class dstat_plugin(dstat):
    def __init__(self):
        self.name = 'stime'
        self.timefmt = '%s'
        self.type = 's'

        if op.debug:
            self.width = len(time.strftime(self.timefmt, time.localtime())) + 4
        else:
            self.width = len(time.strftime(self.timefmt, time.localtime()))
        self.scale = 0
        self.vars = ('time',)

    ### We are now using the starttime for this plugin, not the execution time of this plugin
    def extract(self):
        if op.debug:
            self.val['time'] = time.strftime(self.timefmt, time.localtime(starttime)) + ".%03d" % (round(starttime * 1000 % 1000 ))
        else:
            self.val['time'] = time.strftime(self.timefmt, time.localtime(starttime))

