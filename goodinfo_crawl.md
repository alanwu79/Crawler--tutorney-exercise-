# 爬goodinfo網站每間公司基本資料存進SQLite資料庫

想把Table的資料變成字典，藍底自當Key，白底當Value
![](https://i.imgur.com/SSxucv2.png)



```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3    
```

分2個類別 
一個資料庫，一個爬蟲
```python
class SQLite:
    def __init__(self,db):
        self.db=db
        
    def GetConnect(self):
        self.connect=sqlite3.connect(self.db)
        cur=self.connect.cursor()
        if not cur:
            print('連接數據庫失敗')
        else:
            return cur
        
    def ExecQuery(self,sql,col):    
        cur=self.connect.cursor()
        cur.execute(sql,col)
        self.connect.commit()
        self.connect.close()
```
還有BUG 
抓兩個List，用ZIP結合成字典 
```python
class Crawl:
    def __init__(self,url):
        self.url = url
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
        
    def Gethtml(self):
        res = requests.get(self.url , headers = self.headers)
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,"html.parser")
        accountant = soup.find('table',class_= 'solid_1_padding_2_6_tbl')    
        nobr = list(accountant.find_all('nobr'))
        td = list(accountant.find_all('td'))
        data1 = []
        data2 = [] 
        for i in nobr:
            data1.append(i.text)
            
        for k in range(len(data1)):
            for j in range(len(td)):
                if td[j-1].text == data1[k]:
                    data2.append(td[j].text)
        return dict(zip(data1, data2))
```
先抓1101台泥的基本資料測試
```
company = Crawl('https://goodinfo.tw/StockInfo/BasicInfo.asp?STOCK_ID=1101')
col_all = company.Gethtml()
sql = "INSERT INTO company (id,stocknm) VALUES (?,?)"
col = []
col = col_all["股票代號"], col_all["股票名稱"]
dbnm = 'goodinfo.sqlite'
database = SQLite('goodinfo.sqlite')
database.GetConnect()
database.ExecQuery(sql,col)
```
