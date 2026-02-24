import matplotlib.pyplot as plt
import numpy as np

# 1. 數據設定
labels = ['A', 'B', 'C', 'D']
data1 = [10, 20, 15, 25]  # 第一組數據
data2 = [15, 12, 18, 20]  # 第二組數據

x = np.arange(len(labels)) + 85 # 標籤位置
print (x)
width = 0.35  # 柱子寬度

fig, ax = plt.subplots()

# 2. 繪製並列長條圖
# 第一組向左偏移，第二組向右偏移
for i in range (len(data1)):
    data1[i] = data1[i] * 5
    
rects1 = ax.bar(x - width/2, data1, width, label='Value 1')
rects2 = ax.bar(x + width/2, data2, width, label='Value 2')

# 3. 添加文字、標籤
ax.set_ylabel('Scores')
ax.set_title('Bar chart with two values per position')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
