import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
res = requests.get("https://tutorney.com/api/search/teacher?category=%E5%85%A8%E9%83%A8&address=510%E5%8F%B0%E7%81%A3%E5%BD%B0%E5%8C%96%E7%B8%A3%E5%93%A1%E6%9E%97%E5%B8%82%E6%BA%9D%E7%9A%82%E4%BA%8C%E8%A1%9713-7%E8%99%9F")
data = json.loads(res.text)
clist = data['results']

guid= []
name = []
gender = []
month = []
year = []
skills = []

for pg in range(1,4):
#    print(pg)
    full_url='https://tutorney.com/api/search/teacher?category=%E5%85%A8%E9%83%A8&address=510%E5%8F%B0%E7%81%A3%E5%BD%B0%E5%8C%96%E7%B8%A3%E5%93%A1%E6%9E%97%E5%B8%82%E6%BA%9D%E7%9A%82%E4%BA%8C%E8%A1%9713-7%E8%99%9F'+  str(pg)
    res = requests.get(full_url)
    data = json.loads(res.text)
    clist = data['results']
    
    for w in clist:
            m = w[:24]
            glist=data['results'][m]
            print(glist['_id'])
           # print(glist['frequency'])
            #print(glist['times'])
            print(glist['name'])
            print(glist['isMale'])
            print(glist['birthday']['month'])
            print(glist['birthday']['year'])
            print(glist['skills'][0]['subject'])
            
            g = glist['_id']
            guid.append(g)
            n = glist['name']
            name.append(n)
            f = glist['isMale']
            if f == False:
               gender.append('女')
            else: 
               gender.append('男')
            #gender.append(f)
            m = glist['birthday']['month']
            month.append(m)
            y = glist['birthday']['year']
            year.append(y)
            s = glist['skills'][0]['subject']
            skills.append(s)
            da = {'ID':guid,'姓名':name,'性別': gender, '生日月':month, '生日年':year, '專長':skills}
            
            
#da = {'ID':[guid],'姓名': [name],'性別': [gender], '生日月':[month], '生日年':[year], '專長':[skills]}
#dex = ['ID', '姓名', '性別', '生日月', '生日年','專長']
df = pd.DataFrame(da)

df.to_csv('Tutorney.csv')
    
    
    