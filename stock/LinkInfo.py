import inspect
from time import gmtime,strftime

class infoObj:
    def __init__(self,startDay = '1',startMonth = '0',startYear = '1990'):
        self.para = {}
        frame = inspect.currentframe()
        args,_,_,values =  inspect.getargvalues(frame)
        for arg in args:
            self.para[arg] = values[arg]
            
        setLst = ['endDay','endMonth','endYear']
        date = strftime('%Y,%m,%d',gmtime()).split(',')
        for i,item in enumerate(setLst):
            self.para[item] = date[i]
        del self.para['self']
    def getLinkPara(self):
        return self.para
    def setLinkPara(self,symbol,endDay,endMonth,endYear,startDay,startMonth,startYear):
        self.para = {}
        frame = inspect.currentframe()
        args,_,_,values =  inspect.getargvalues(frame)
        for arg in args:
            self.para[arg] = self.args.get(arg,'') + values[arg]
