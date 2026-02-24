import pandas as pd

# 1. 讀取時跳過開頭的前 N 行 (假設前 3 行是雜質)
# 2. 如果結尾是不固定的文字，通常讀入後再處理
df = pd.read_excel('car-all-oil-e.xlsx', skiprows=3)

# 3. 處理結尾：
# 如果結尾文字所在行包含很多 NaN，可以使用 dropna 移除整列都是空的行
# 或者根據特定欄位是否有值來篩選
#df_cleaned = df.dropna(how='all') 
#df.iloc[0,0]='year'
df_cleaned = df.dropna()
df_cleaned = df_cleaned.replace('-', 0)
#df_cleaned = df_cleaned.replace('/', '_')

# 4. 如果知道表格確切的長度，也可以用 head() 
# df_cleaned = df_cleaned.head(10) # 只取前10列

# 轉成 2D List
data_2d = df_cleaned.values.tolist()
#print(data_2d)

#print ()

df_cleaned['total-car-all-oil']=0
for i in range (0, len(df_cleaned)):
    df_cleaned.loc[i, 'total-car-all-oil']=int(df_cleaned.loc[i, '汽油_新北市'])+int(df_cleaned.loc[i, '汽油_臺北市'])+\
int(df_cleaned.loc[i, '柴油_新北市'])+int(df_cleaned.loc[i, '柴油_臺北市'])+\
int(df_cleaned.loc[i, '液化石油氣_新北市'])+int(df_cleaned.loc[i, '液化石油氣_臺北市'])+\
int(df_cleaned.loc[i, '汽油/LPG_新北市'])+int(df_cleaned.loc[i, '汽油/LPG_臺北市'])
nCartotal_detail_oil=list(df_cleaned['total-car-all-oil'])
print(nCartotal_detail_oil)

df_cleaned['total-car-all-e']=0
for i in range (0, len(df_cleaned)):
    df_cleaned.loc[i, 'total-car-all-e']=int(df_cleaned.loc[i, '電能_新北市'])+int(df_cleaned.loc[i, '電能_臺北市'])+\
int(df_cleaned.loc[i, '汽油/電能_新北市'])+int(df_cleaned.loc[i, '汽油/電能_新北市'])+\
int(df_cleaned.loc[i, '柴油/電能_新北市'])+int(df_cleaned.loc[i, '柴油/電能_臺北市'])+\
int(df_cleaned.loc[i, '電能/汽油_新北市'])+int(df_cleaned.loc[i, '電能/汽油_臺北市'])+\
int(df_cleaned.loc[i, '電能/柴油_新北市'])+int(df_cleaned.loc[i, '電能/柴油_臺北市'])+\
int(df_cleaned.loc[i, '電能/柴油_臺北市'])+int(df_cleaned.loc[i, '電能(增程)_臺北市'])+\
int(df_cleaned.loc[i, '汽油(油電)_新北市'])+int(df_cleaned.loc[i, '汽油(油電)_臺北市'])+\
int(df_cleaned.loc[i, '柴油(油電)_新北市'])+int(df_cleaned.loc[i, '柴油(油電)_臺北市'])+\
int(df_cleaned.loc[i, '汽油(電能)_新北市'])+int(df_cleaned.loc[i, '汽油(電能)_臺北市'])
nCartotal_detail_e=list(df_cleaned['total-car-all-e'])
print(nCartotal_detail_e)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(14)+101  

fig, ax = plt.subplots()

#ax.figure(figsize=(15, 6))
ax.set_title('Electric / Oil (totals of car)')
ax.set_xlabel("Year")
ax.set_ylabel('values(million)')
width = 0.35
#listTotals.insert(0, 0)
ax.bar(x + width/2, nCartotal_detail_oil, width, label='Oil')
ax.bar(x - width/2, nCartotal_detail_e, width, label='E')
ax.legend()
ax.plot(x + width/2, nCartotal_detail_oil, 'g--', x - width/2, nCartotal_detail_e, 'r--')

plt.show()


