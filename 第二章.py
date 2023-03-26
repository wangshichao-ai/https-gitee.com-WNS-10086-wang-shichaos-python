#2.2程序实例
#question1:有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
L=[]
a=[1,2,3,4]
 
#for i in range(len(a)):
 
for val_1 in a:   #   for(i=1;i<n;I++)
    for val_2 in a:
        for val_3 in a:
            if(val_1 == val_2 or val_1 == val_3 or val_2 == val_3):
                continue
            else:
                L.appendstr(val_1)+str(val_2)+str(val_3)
 

print(len(L)) 
print (L)
###
n=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                n=n+1
                print (i,j,k,"n=",n)

#question2:企业发放的奖金根据利润提成。 利润(I)低于或等于10万元时，奖金可提10%； 
# 利润高于10万元，低于20万元时，低于10万元的部分 按10%提成，高于10万元的部分，可提成7.5%； 
# 20万到40万之间时，高于20万元的部分，可提成5%；
#  40万到60万之间时高于40万元的部分，可提成3%； 
# 60万到100万之间时，高于60万元的部分，可提成1.5%;
#  高于100万元时,超过100万元的部分按1%提成。
#  从键盘输入当月利润I，求应发放奖金总数？
profit = 0
I = int(input("please input: "))
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
###
#int（x）将x转换为一个整数
#float（x)将X转换为一个浮点数
#complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0
#complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式

#2.3程序的基本结构
#a.顺序结构  b.分支结构  c.循环结构

#2.4顺序结构
#数字函数：
    #abs(x)---返回数字的绝对值，如abs(-10) 返回 10
    #ceil(x)---返回数字的上入整数，如math.ceil(4.1) 返回 5
    #cmp(x, y)---如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换
    #exp(x)---返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
    #fabs(x)---	返回数字的绝对值，如math.fabs(-10) 返回10.0
    #floor(x)---返回数字的下舍整数，如math.floor(4.9)返回 4
    #log(x)---如math.log(math.e)返回1.0,math.log(100,10)返回2.0
    #max(x1, x2,...)---返回给定参数的最大值，参数可以为序列
    #min(x1, x2,...)---返回给定参数的最小值，参数可以为序列
    #modf(x)---返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
    #pow(x, y)---x*y 运算后的值
    #round(x [,n])---返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
    #sqrt(x)---返回数字x的平方根
#随机数函数
    #choice(seq)---从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数
    #randrange ([start,] stop [,step])---从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
    #random()---随机生成下一个实数，它在[0,1)范围内
    #seed([x])---改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed
    #shuffle(lst)---将序列的所有元素随机排序
    #uniform(x, y)---随机生成下一个实数，它在[x,y]范围内
#三角函数
    #acos(x)---返回x的反余弦弧度值
    #atan2(y, x)---返回给定的 X 及 Y 坐标值的反正切值
    #hypot(x, y)---返回欧几里德范数 sqrt(x*x + y*y)
    #degrees(x)---将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
    #radians(x)---	将角度转换为弧度
#数学常量
    #pi---数学常量 pi（圆周率，一般以π来表示）

#exanple：绘制计算圆周长的流程图
import graphviz
dot=graphviz.Digraph(comment='the round table',name="顺序结构",node_attr={'shape': 'box'})
dot.node('1','Start')
dot.node('2','input Radius =?',shape='parallelogram')
dot.node('3','Print Radius')
dot.node('4','Caculating Area')
dot.node('5','Caculating perimeter')
dot.node('6','print')
dot.node('7','end')
dot.edges(['12','23','34','45','56','67'])
dot