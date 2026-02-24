import pandas as pd

# 1. 讀取時跳過開頭的前 N 行 (假設前 3 行是雜質)
# 2. 如果結尾是不固定的文字，通常讀入後再處理
df = pd.read_excel('Total-Car.xlsx', skiprows=3)

# 3. 處理結尾：
# 如果結尾文字所在行包含很多 NaN，可以使用 dropna 移除整列都是空的行
# 或者根據特定欄位是否有值來篩選
#df_cleaned = df.dropna(how='all') 
#df.iloc[0,0]='year'
df_cleaned = df.dropna()
df_cleaned = df_cleaned.replace('-', 0)

# 4. 如果知道表格確切的長度，也可以用 head() 
# df_cleaned = df_cleaned.head(10) # 只取前10列

# 轉成 2D List
data_2d = df_cleaned.values.tolist()
#print(data_2d)

#print ()

df_cleaned['total']=0
for i in range (1, len(df_cleaned)):
    df_cleaned.loc[i, 'total']=int(df_cleaned.loc[i, '總計_新北市'])+int(df_cleaned.loc[i, '總計_臺北市'])
        
nCartotal=list(df_cleaned['total'])