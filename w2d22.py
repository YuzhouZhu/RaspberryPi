#~ yuzhou zhu_w2d2 2

def computepay (Hours, RPH):
    if Hours < 40:
        pay = RPH*Hours
    else:
        pay = 40*RPH + 1.5*RPH*(Hours-40)
    return pay

Hours = int(input("Please enter the number of hours: "))
RPH = int(input("Please enter the rate per hour: "))        
pay = computepay (Hours, RPH)

print("PAY:",pay,"$") 