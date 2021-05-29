#~ yuzhou zhu_w2d2 1

Hours = int(input("Please enter the number of hours: "))
RPH = int(input("Please enter the rate per hour: "))

if Hours < 40:
    pay = RPH*Hours
else:
    pay = 40*RPH + 1.5*RPH*(Hours-40)
print("PAY:",pay,"$") 
