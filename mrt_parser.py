
import requests
import pandas as pd

def crawl_metro_monthly_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # 1. 抓取網頁原始資料
        response = requests.get(url, headers=headers)
        #response = requests.get(url)
        response.encoding = 'big5'
        
        
        # 2. 解析 HTML 表格
        dfs = pd.read_html(response.text)
        if not dfs:
            return "找不到表格資料"
            
        # 取得主表格
        df = dfs[0]

        # 3. 處理 NaN 並轉換為二維列表
        # 將所有 NaN 替換為空字串 ""
        df_filled = df.fillna("")
        
        header = df_filled.columns.tolist()
        data_body = df_filled.values.tolist()
        
        # 結合標題與內容
        two_dim_table = [header] + data_body        
        
        #return two_dim_table
        i=-1
        while two_dim_table[i][0] != '當月總計':
            i = i - 1
            if (-i == len(two_dim_table)):
                #debug
                print ("issue page:", url)
                for row in two_dim_table[-5:]:
                    print(row)
                    
                return two_dim_table, 0
            
        listAns=two_dim_table[i]
        #print (listAns)
        nTotal=int(listAns[2])
        #print(nTotal)
        
        return two_dim_table, nTotal

    except Exception as e:
        return f"爬取失敗: {e}"

# 執行與驗證
#if __name__ == "__main__":
#1.MRT data, from 85 to 114 (month:01~12)    
#1.1 create dataframe for MRT data
list1=[0,0,0,0, 0,0,0,0, 0,0,0,0, 0]
dfMRT=pd.DataFrame()  

target_url = 'https://web.metro.taipei/RidershipCounts/c/11401.htm'
target_url_0 = 'https://web.metro.taipei/RidershipCounts/c/'

for i in range (85, 115):
#for i in range (85, 87):    
    dfMRT[str(i)] = list1
    nYearTotal=0
    for j in range (1, 13):
        strDay=f"{j:02d}"    
        target_url = target_url_0+str(i)+strDay+'.htm'
        print(target_url)
        
        #special process: 8501, 8502
        if (i == 85) and (j == 1 or j == 2):
            dfMRT.loc[(j-1),str(i)] = 0
            continue
        
        result, nData = crawl_metro_monthly_data(target_url)
        #print ('nData=', nData) #debug
        
        if isinstance(result, list):
            #print("--- 資料擷取成功（含統計行且已處理 NaN） ---")
            dfMRT.loc[(j-1),str(i)] = nData
            nYearTotal=nYearTotal + nData
        else:
            print("--- 資料擷取: FAIL! ---")
            dfMRT.loc[(j-1),str(i)] = 0
    dfMRT.loc[12,str(i)]=nYearTotal 

listTotals=list(dfMRT.loc[12])
print ("totals: ",listTotals)

#%%
#get motocycle data
import xlsx_parser as moto
print (moto.nMotototal)

#%%
#get car data
import xlsx_parser_car as car
print (car.nCartotal)

for i in range(17, 31):
    moto.nMotototal[i]= moto.nMotototal[i]+car.nCartotal[i-17]

#%%
#draw bar plots
import matplotlib.pyplot as plt
import numpy as np
#data
x = np.arange(31)+84    
y = [11112222, 2222333, 33334444, 44445555, 55556666, 66667777, 77778888, 88889999, 99990000, 12345678,
11112222, 2222333, 33334444, 44445555, 55556666, 66667777, 77778888, 88889999, 99990000, 12345678,
11112222, 2222333, 33334444, 44445555, 55556666, 66667777, 77778888, 88889999, 99990000, 12345678]

#pre-process to enlarge moto data
nScale=100
nMotototal=moto.nMotototal
for i in range (len(nMotototal)):
    nMotototal[i] = nMotototal[i] * nScale

#print ("x:", x)
#xlim = list(map(str, x))

fig, ax = plt.subplots()

#ax.figure(figsize=(15, 6))

ax.set_xlabel("Year")
ax.set_ylabel('values(million)')
width = 0.35
listTotals.insert(0, 0)
ax.bar(x + width/2, listTotals, width, label='MRT')
ax.bar(x - width/2, moto.nMotototal, width, label='Moto')
ax.legend()
ax.plot(x + width/2, listTotals, 'g--', x - width/2, moto.nMotototal, 'r--')

plt.show()


        