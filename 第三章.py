#3.2序列类型
     #3.2.1字符串运算
a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
# in 
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
print (r'\n')
print (R'\n')
###
     #a + b 输出结果： HelloPython
     #a * 2 输出结果： HelloHello
     #a[1] 输出结果： e
     #a[1:4] 输出结果： ell
     #H 在变量 a 中
     #M 不在变量 a 中
     #\n
     #\n

#3.2.2元组
     #Python 的元组与列表类似，不同之处在于元组的元素不能修改,可以合并。
     #元组使用小括号 ( )，列表使用方括号 [ ]。
     #元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"   #  不需要括号也可以
type(tup3)
print(tup1,"\n","tup2","\n",tup3,"\n",type(tup3))

print(id(tup1))
tup1=1,2,3
print(id(tup1))

#3.2.3列表
     #序列是 Python 中最基本的数据结构。
     #序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。
     #Python 有 6 个序列的内置类型，但最常见的是列表和元组。
     #列表都可以进行的操作包括索引，切片，加，乘，检查成员。
     #此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。
     #列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。
     #列表的数据项不需要具有相同的类型
     #创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可

list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[-3] )
print( list[-2] )
print( list[-1] )
#从前往后数为0，1，2;从后往前数为-1，-2，-3
###

list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
# 读取第二位
print ("list[0]: ", list[0])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[0:4]: ", list[0:5])
###

list[2] = 2001
print ("更新后的第三个元素为 : ", list)
list.append('Baidu')
print ("更新后的列表 : ", list)
list[:]=''
###

print(list)
###

#Python列表函数&方法
     #函数；  #len(list)--列表元素个数
             #max(list)--返回列表元素最大值
             #min(list)--返回列表元素最小值
             #list(seq)--将元组转换为列表
     #方法：  #list.append(obj)--在列表末尾添加新的对象
             #list.count(obj)--统计某个元素在列表中出现的次数
             #list.extend(seq)--在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
             #list.index(obj)--从列表中找出某个值第一个匹配项的索引位置
             #list.insert(index, obj)--将对象插入列表
             #list.pop([index=-1])--移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
             #list.remove(obj)--移除列表中某个值的第一个匹配项
             #list.reverse()--反向列表中元素
             #list.sort( key=None, reverse=False)--对原列表进行排序
             #list.clear()--清空列表
             #list.copy()--复制列表

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)
###

cars.pop()
print(cars)
###

#3.3集合类型
         #集合（set）是一个无序的不重复元素序列。
         #可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典 
     #3.3.1基本操作；
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(len(basket))                      # 这里演示的是去重功能    
###

{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # 快速判断元素是否在集合内
###

'crabgrass' in basket
###

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print('a=',a)
print('b=',b)
# 集合a中包含而集合b中不包含的元素 
a - b  
###

# 集合a或b中包含的所有元素（并集）
a | b 
###

# 不同时包含于a和b的元素（交集的补集）
a ^ b 
###

#类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x  for x in 'abracadabra' if x not in 'abc'}
print(a)
###

#3.3.2集合运算
     #add()----为集合添加元素
     #clear()----移除集合中的所有元素
     #copy()----	拷贝一个集合
     #difference()----返回多个集合的差集
     #difference_update()----移除集合中的元素，该元素在指定的集合也存在
     #discard()----	删除集合中指定的元素
     #intersection()----	返回集合的交集
     #intersection_update()----返回集合的交集
     #isdisjoint()----判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
     #issubset()----判断指定集合是否为该方法参数集合的子集
     #issuperset()----	判断该方法的参数集合是否为指定集合的子集
     #pop()----	随机移除元素
     #remove()----	移除指定元素
     #symmetric_difference()----返回两个集合中不重复的元素集合
     #symmetric_difference_update()----移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
     #union()----返回两个集合的并集
     #update()----给集合添加元素

# 增加
basket.add("Facebook")
print(basket)
# 添加
basket.update("Facebook")
print(basket)
# 删除
#basket.remove("apple")
print(basket)
#basket.remove('none')  # throw error!!!
basket.discard('none') # don't throw error!!!
basket.pop()# throw one element random
###

# 计算集合长度
basket.pop()
print(basket)
len(basket)
###

