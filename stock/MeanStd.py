import csv,LinkInfo,numpy,urllib2,os

class DataMeanStd:
    '''
    #(a,b,c) beginning month(0 index base),day,year 
    #(d,e,f) ending month(0 index base),day,year 
    #(s) symbol 
    '''
    def constructLink(self,linkDict,symbol):
        link = 'http://real-chart.finance.yahoo.com/table.csv?s={0}&d={1}&e={2}&f={3}&g=d&a={4}&b={5}&c={6}&ignore=.csv'.format(symbol,linkDict['endDay'],
                               linkDict['endMonth'],linkDict['endYear'],
                               linkDict['startDay'],linkDict['startMonth'],linkDict['startYear'])
        return link
    
    def getCompanyLst(self):
        path = os.path.abspath(os.pardir).split('/')[:-1]
        path = '/'.join(path)
        path += '/companylist.txt'
        with open(path,'r') as f:
            for line in f:
                yield(line.strip())

    def getCsvFiles(self,infoObj):
        res  = {}
        paraLst = infoObj.getLinkPara()
     
        for symbol in  self.getCompanyLst():
            numLst = []
            link = self.constructLink(paraLst,symbol)
            try:
                print(symbol)
                response =  urllib2.urlopen(link)
                f = csv.reader(response)
                for i,line in enumerate(f):
                    if i == 0: continue
                    numLst.append(float(line[-1]))
                numLst = [ float(i[0])/float(i[1]) -1 for i in zip(numLst[0:],numLst[1:])]
                price = numpy.array(numLst)
                res[symbol] = [numpy.mean(price),numpy.std(price)]
            except:
                print('error for {0} link'.format(symbol))
        #npArray = numpy.array(numLst)
        with open('MeanStdData.txt','w') as f:
            for k,v in res.items():
                print >> f,(k,v)
                return res
                
    def run(self):
        infoObj = LinkInfo.infoObj()
        self.getCsvFiles(infoObj)
        
if __name__ == '__main__':
    x = DataMeanStd()
    x.run()
    
