profit = 0
I =int(input("please input:100 "))
if(I<=10):
    profit = 0.1 * I
elif(I <= 20):
    profit = 10 *0.1 + (I - 10)*0.075
elif(I <=40):
    profit = 10 * 0.1 + (20 - 10)*0.075 + (I - 20)*0.05
elif(I <= 60):
    profit = 10 * 0.1 + (20 - 10)*0.075 + (40 - 20)*0.05 + (I - 40)*0.03
elif(I <= 100):
    profit = 10 * 0.1 + (20 - 10)*0.075 + (40 - 20)*0.05 + (60 - 40)*0.03 + (I - 60)*0.015
else : 
    profit = 10 * 0.1 + (20 - 10)*0.075 + (40 - 20)*0.05 + (60 - 40)*0.03 + (100 - 60)*0.015 + (I -100)*0.01
        
print ("profit=",profit)
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]#r=r+nnn
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print ("profit=",r)