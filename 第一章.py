#1.1数字常量
#python支持int,float,bool,complex(复数)
#只有int表示为长整型
z=2+5j
type (z)
print(z.conjugate())
###

pow(3,600)
###
import sys
print (sys.float_info)
print(sys.int_info)
###

#1.2标准数据类型
#number 数字；string 字符串；list 列表;tuple 元组;set 集合；dictionary 字典
#python的6个标准数据类型：
counter =100#整型变量
miles = 1000.0#浮点型变量
name ="ru 'n'oob"#字符串(string,不可变数据)
name2='xauat"edu"'
name3='''a
b
  c'''
tup1=(1,2,3,4,5)#元组(tuple，不可变数据)
number=(123456)#数字（number，不可变数据)
list1=[12,3,4,5]#列表(list，可变数据)
dict ={'name':'王世超','age':19,'mail':'2216238538@qq.com'}#字典(dictionary，可变数据)
basket={'apple','banana','pear','orange'}#集合(set，可变数据)
print (counter)
print(miles)
print(name)
print(basket)
###

#1.3数字类型的操作
#数值计算+ - * /
a = b = 1
c=a+b
print("a+b=", c)
c=a*b
print("a*b=", c)
a=8
b=3
c=a/b
print("a/b=", c)
c=a//b
print("a//b=", c)
c = a%b
print("a%b =", c)
c = a ** b
print("a**b=", c)
###

#1.4 字符串变量操作
#可以使用引号( ' 、 " 或 ''')来创建字符串
var1 = 'Hello World!'
var2 = "Runoob"
var3='''Hello World '''
#Python 访问字符串中的值 Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
#Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下： `print(var1[1:5])'
