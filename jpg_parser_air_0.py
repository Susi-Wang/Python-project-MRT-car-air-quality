import pandas as pd
#import numpy as np

# 根據圖片「表 3-2-1 歷年測站年平均濃度統計表」解析的數據
# 欄位定義：[年份, PM10, SO2, NO2, CO, O3, PM2.5]
raw_data_321 = [
    ["103年", 40.9, 3.00, 20.65, 0.87, 25.34, None],
    ["104年", 36.0, 3.07, 23.39, 0.86, 26.55, None],
    ["105年", 31.7, 2.42, 21.64, 0.80, 23.76, None],
    ["106年", 34.0, 2.24, 19.32, 0.75, 24.11, 15.8],
    ["107年", 32.7, 1.76, 18.10, 0.75, 25.25, 17.2],
    ["108年", 31.5, 1.52, 16.62, 0.72, 25.11, 15.6],
    ["109年", 29.4, 1.02, 15.76, 0.67, 24.90, 13.5],
    ["110年", 31.3, 0.98, 14.62, 0.61, 25.24, 14.0],
    ["111年", 26.9, 0.94, 13.81, 0.61, 25.72, 11.4],
    ["112年", 31.4, 0.93, 13.06, 0.59, 25.91, 11.2]
]

def create_air_quality_dataframe(data):
    # 定義欄位名稱與對應單位
    columns = [
        "Year", 
        "PM10 (μg/m3)", 
        "SO2 (ppb)", 
        "NO2 (ppb)", 
        "CO (ppm)", 
        "O3 (ppb)", 
        "PM2.5 (μg/m3)"
    ]
    
    # 建立 DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # 將數據類型轉換為浮點數，None 會自動變更為 NaN
    numeric_cols = df.columns[1:]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
    
    return df

# 執行轉換
df_112 = create_air_quality_dataframe(raw_data_321)

# 顯示結果
print("--- 表 3-2-1 歷年測站年平均濃度統計表 (103-112年) ---")
print(df_112)

#%%
import pandas as pd
import pytesseract
from PIL import Image
#import io

# 如果是 Windows 系統，可能需要指定 tesseract.exe 的路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def parse_table_to_df(image_path):
    """
    讀取圖片並透過 OCR 轉為 DataFrame
    """
    # 1. 讀取圖片並進行 OCR 辨識 (指定繁體中文與英文)
    # config 參數 --psm 6 假設圖片為單一區塊的文本表格
    text_data = pytesseract.image_to_string(Image.open(image_path), lang='chi_tra+eng', config='--psm 6')
    
    # 2. 清理與結構化數據 (這部分通常需要根據 OCR 結果微調)
    lines = [line.strip().split() for line in text_data.split('\n') if line.strip()]
    
    # 3. 建立 DataFrame
    df = pd.DataFrame(lines)
    return df

file_n= './a112t_1.jpg'
df=parse_table_to_df(file_n)
print(df)