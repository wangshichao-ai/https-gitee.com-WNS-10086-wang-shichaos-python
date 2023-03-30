a = "love you three thousand times,"
b = " my Argentina girl"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("b[5] 输出结果：", b[5])
print("a[3:15] 输出结果：", a[3:15])
###

a= "love you thousand times" 
#in
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
#not in 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")

# r R 直接打印字符串 
print (R'\2216238538@qq.com')
print (R'\i will go where no one goes')
###

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"  
type(tup3)
print(tup1,"\n","tup2","\n",tup3,"\n",type(tup3))

print(id(tup1))
tup1=1,2,3
print(id(tup1))
