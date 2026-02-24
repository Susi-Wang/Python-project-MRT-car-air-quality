1.主要程式: mrt_parser.py: 取得捷運歷年搭乘人員的數量,繪製Matplotlib-Bar圖
1.1 副程式: xlsx_parser.py: 取得台北市及新北市機車總數量(data file=Total_Moto3.xlsx)
1.2 副程式: xlsx_parser_car.py: 取得台北市及新北市汽車總數量(data file=Total-Car.xlsx)
> 組合顯示出page-7, page-10(放大汽機車數量)的圖表

2.主要程式: car_moto_oil_e_comparsion.py: 統計台北市及新北市的(汽機車)油車與電動車的數量
> 顯示出page-12的圖表
2.1 副程式: xlsx_parser_moto_detail.py: 將機車的油車及電動車數量分開統計數量(data file=moto-all-oil-e.xlsx)
> 顯示出page-11上方的圖表
2.2 副程式: xlsx_parser_car_detail.py: 將汽車的油車及電動車數量分開統計數量(data file=car-all-oil-e.xlsx)
> 顯示出page-12下方的圖表

3.主要程式: car_moto_oil_e_comparsion_air.py: 統計台北市及新北市的(汽機車)油車與電動車的數量,及空氣品質的二氧化硫/PM2.5數值
> 顯示出page-13的圖表
3.1 副程式: jpg_parser_air.py: 取得空氣品質的二氧化硫/PM2.5數值(data file=a112t.jpg)
3.2 失敗的副程式: jpg_parser_air_0.py: 取得空氣品質的二氧化硫/PM2.5數值(data file=a112t.jpg)

4.參考範例: bar2line.py: Matplotlib-Bar圖,一個X位置並列顯示兩個資料的範例程式
5.參考檔案: 
> 108年台北市空氣品質報告書.pdf
> 109年台北市空氣品質報告書.pdf
> 110年台北市空氣品質報告書.pdf
> 111年台北市空氣品質報告書.pdf
> 112年台北市空氣品質報告書.pdf
6.sub-folder 'reference': 放置官方文件中的圖表,報告時備用