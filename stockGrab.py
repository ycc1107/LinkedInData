import urllib2,os,sys,threading,collections,subprocess 
from time import gmtime, strftime
from BeautifulSoup import BeautifulSoup


class CrawlData(threading.Thread):
	def __init__(self,threadId,dataLst):
		threading.Thread.__init__(self)
		self.threadId = threadId + 1
		self.dataLst = dataLst
		self.status = 0.0

	def run(self):
		print('Thread {0} begin'.format(self.threadId))
		self.length = len(self.dataLst)
		self.getLinkData()

	def getLinkData(self):
		fixedLinkPre = "http://finance.yahoo.com/q/ks?s="
		fixedLinkPost = "+Key+Statistics"
		for self.index,self.stock in enumerate(self.dataLst):
			link = fixedLinkPre+self.stock+fixedLinkPost
			response = urllib2.urlopen(link)
			self.html = response.read()
			response.close()
			self.cleanHtml()
			self.writeFile()
			self.status = 1.0*(self.index+1)/len(self.dataLst)
	
	def getThreadInfo(self):
		return (self.threadId,self.status)

	def cleanHtml(self):
		self.cleanData = []
		soup = BeautifulSoup(self.html)
		tagName = soup.findAll('td',{'class':'yfnc_tablehead1'})
		tagValue = soup.findAll('td',{'class':'yfnc_tabledata1'})
		self.cleanData = list(map(lambda x: x[0].text + ' ' + x[1].text),zip(tagName,tagValue))
		'''
		for item in zip(tagName,tagValue):
			value = item[0].text+' '+item[1].text
			if value:
				self.cleanData.append(value)
		'''
	def writeFile(self):
		if len(self.cleanData):
			dirName = os.path.dirname(os.path.abspath(__file__))
			dirName = os.path.join(dirName,"Data")
			folder = strftime("%Y-%m-%d", gmtime()) 
			path = os.path.join(dirName,folder)

			if not os.path.exists(path):
				os.makedirs(path)
				
			fileName = os.path.join(path,(self.stock + ".txt"))
			try:
				with open(fileName,"w") as f:
					for line in self.cleanData:
						print >> f,line
			except:
				print("Writing failure on %s" %self.stock)
			
class ReadData:
	def readInStockData(self):
		stockData = []
		with open("companylist.txt","r") as f:
			for company in f:
				stockData.append(company.strip())
		return stockData
			
class ReadData:
	def readInStockData(self):
		stockData = []
		with open("companylist.txt","r") as f:
			for company in f:
				stockData.append(company.strip())
		return stockData

def showThePercentage(process):
	subprocess.call('cls',shell=True)
	for threadId,status in enumerate(process):
		currentStarNum = int(30*status)
		star = ("*"*(currentStarNum + 1)).ljust(30)
		sys.stdout.write('{0}:{1} ...[{3}] {2}%\n'.format('Thread ID:',threadId+1,int(1000*status)/10.0,star))
	sys.stdout.flush()


if __name__ == "__main__":
	threadNum = 8
	read = ReadData()
	dataLst = read.readInStockData()
	increament,start = len(dataLst)//8 , 0
	threadLst = []

	for i in range(threadNum):
		threadLst.append(CrawlData(i,dataLst[start:(start+increament)]))
		start += increament
	for thread in threadLst:
		thread.start()
	
	while any(thread.is_alive() for thread in threadLst):
		process = []
		for thread in threadLst:
			threadId,status = thread.getThreadInfo()
			process.append(status)
		showThePercentage(process)
	print('All thread done!')
