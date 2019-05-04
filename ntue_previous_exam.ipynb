import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Crawl:
    def __init__(self, url):
        self.url = url       
        self.resp = None
        self.soup = None 
        self.a_tag = None
        self.pdf_dir = "pdfs/"
        self.full_path = None
        
    def Parser(self):
        self.resp = requests.get(self.url) 
        self.resp.encoding='utf-8'
        self.soup = BeautifulSoup(self.resp.text,"html.parser")

    def Combinelink(self):
        if not os.path.exists(self.pdf_dir):
            os.mkdir(self.pdf_dir)
        self.a_tag = self.soup.find_all("a")
        for a_tag in self.a_tag :
            href=a_tag.get("href")
            if (href == None or href.split('.')[-1]!='pdf'):
                continue;
            if(href[0:4]=='http'):
                self.full_path = href
            elif(href[0]=='/'):
                self.full_path = "http://academic.ntue.edu.tw" + href
            else:
                self.full_path = "http://academic.ntue.edu.tw/ezfiles/" + href
            print(self.full_path)
            
            try:
                filename = self.full_path.split('/')[-1]
                pdf = urlopen(self.full_path)
                f = open(os.path.join(self.pdf_dir,filename),'wb')
                f.write(pdf.read())
                f.close()
            except:
                print ("{} 無法讀取!".format(filename))
   

C1 = Crawl('http://academic.ntue.edu.tw/files/11-1007-467.php')
C1.Parser()
C1.Combinelink()
