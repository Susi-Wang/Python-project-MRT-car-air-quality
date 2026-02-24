#get Taipei air data (Year 103~112)
import jpg_parser_air as air
listSo2=air.listSo2
listPm25=air.listPm25
##fill Y101~102 data as zero
for i in range (2):
    listSo2.insert(0, 0)
    listSo2.append(0)
    listPm25.insert(0, 0)
    listPm25.append(0)
print (listSo2)
print (listPm25)

##pre-process to enlarge moto data
nScale=150000
for i in range (len(listSo2)):
    listSo2[i] = listSo2[i] * nScale*2
    listPm25[i] = listPm25[i] * nScale
    
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
width = 0.2
#listTotals.insert(0, 0)
ax.bar(x - width*3/2, nTotal_e, width, label='Electric')
ax.bar(x - width/2, nTotal_oil, width, label='Oil')
ax.bar(x + width*3/2, listSo2, width, label='air-SO2')
ax.bar(x + width/2, listPm25, width, label='air-PM2.5')
ax.legend()
#ax.plot(x - width/2, nTotal_e, 'g--', x - width/4, nTotal_oil, 'r--')
ax.plot(x - width/2, nTotal_e, 'g--', x - width/4, nTotal_oil, 'r--', x + width/4, listPm25, 'k--', x + width/2, listSo2, 'c--')

plt.show()