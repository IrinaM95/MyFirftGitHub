# Вычисление количества продаж и среднего чека в интервалах: 
# До 1000 р включительно
# От 1000 р до 3000 р включительно
# От 3000 р до 5000 р включительно
# Выше 5000 р.

sales = [2033, 300.50, 1550, 2703, 5110, 2146, 4733, 7114, 1614, 3105, 3155, 853, 10114, 1315]

def process_sales(sales):
    #Sum
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    #Количества
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    #Средние
    avg1 = 0
    avg2 = 0
    avg3 = 0
    avg4 = 0
    for sale in sales:
       print(sale, end=' ')
       if sale <= 1000:
          sum1 += sale
          cnt1 += 1
       elif sale<=3000:
          sum2 += sale
          cnt2 += 1
       elif sale<=5000:
          sum3 += sale
          cnt3 += 1
       else:
          sum4 += sale
          cnt4 += 1
    print("")  
    
    if cnt1 > 0: #Иначе оставляем avg1 равным 0
        avg1 = sum1 / cnt1
    if cnt2 > 0: #Иначе оставляем avg2 равным 0
        avg2 = sum2 / cnt2   
    if cnt3 > 0: #Иначе оставляем avg3 равным 0
        avg3 = sum3 / cnt3
    if cnt4 > 0: #Иначе оставляем avg4 равным 0
        avg4 = sum4 / cnt4   
           
    print("До 1000 р включительно = " + str(cnt1) + " прод., Средний чек = " + "{:.2f}".format(avg1) + "р.")
    print("От 1000 р до 3000 р включительно = " + str(cnt2) + " прод., Средний чек = " + "{:.2f}".format(avg2) + "р.")
    print("От 3000 р до 5000 р включительно = " + str(cnt3) + " прод., Средний чек = " + "{:.2f}".format(avg3) + "р.")
    print("Выше 5000 р. = " + str(cnt4) + " прод., Средний чек = " + "{:.2f}".format(avg4) + "р.")  
    
    print("Готово!")  

process_sales(sales)

