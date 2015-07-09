import urllib2,os,sys
from time import gmtime, strftime

class CrawlData:
	def run(self):
		self.readInStockData()
		self.length = len(self.stockData)
		self.getLinkData()

	def showThePercentage(self):
		currentStarNum = int(30*self.index/self.length)
		star = "*"*(currentStarNum + 1)
		#print(star,currentStarNum,self.length)
		sys.stdout.write('Working... '+str(int(1000*self.index/self.length)/10.0)+'% '+star+'\r')
    	sys.stdout.flush()


	def readInStockData(self):
		self.stockData = []
		with open("companylist.txt","r") as f:
			for company in f:
				self.stockData.append(company.strip())

	def writeFile(self):
		dirName = os.path.dirname(os.path.abspath(__file__))
		dirName = os.path.join(dirName,"Data")
		folder = strftime("%Y-%m-%d", gmtime()) 
		path = os.path.join(dirName,folder)

		if not os.path.exists(path):
			os.makedirs(path)

		fileName = os.path.join(path,(self.stock + ".txt"))
		try:
			file(fileName,"w").write(self.html)
		except:
			print("Writing failure on %s" %self.stock)

	def getLinkData(self):
		fixedLinkPre = "http://finance.yahoo.com/q/ks?s="
		fixedLinkPost = "+Key+Statistics"
		for self.index,self.stock in enumerate(self.stockData):
			link = fixedLinkPre+self.stock+fixedLinkPost
			response = urllib2.urlopen(link)
			self.0
			response.close()
			self.writeFile()
			self.showThePercentage()
			

if __name__ == "__main__":
	getData = CrawlData()
	getData.run()
