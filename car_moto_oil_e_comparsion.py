
#get car data
import xlsx_parser_car_detail as car

#get motocycle data
import xlsx_parser_moto_detail as moto

#add oil-car and moto
nTotal_oil=[]
for i in range (len(car.nCartotal_detail_oil)):
    nTotal_oil.append(car.nCartotal_detail_oil[i] + moto.nMotototal_detail_oil[i])

nTotal_e=[]
for i in range (len(car.nCartotal_detail_oil)):
    nTotal_e.append(car.nCartotal_detail_e[i] + moto.nMotototal_detail_e[i])

#draw plot
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(14)+101-100+2011  

fig, ax = plt.subplots()

#ax.figure(figsize=(15, 6))


ax.set_title('Electric / Oil (totals of car and moto)')
ax.set_xlabel("Year")
ax.set_ylabel('values(million)')
width = 0.35
#listTotals.insert(0, 0)
ax.bar(x + width/2, nTotal_e, width, label='Electric')
ax.bar(x - width/2, nTotal_oil, width, label='Oil')
ax.legend()
ax.plot(x + width/2, nTotal_e, 'g--', x - width/2, nTotal_oil, 'r--')

plt.show()