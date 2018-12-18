#闭包操作1
'''
def py02():
    #局部变量
    girl='李莎莎'
    boy='高波'
    yao='晶晶'

    #内部函数
    def tiaowu():
        print('李莎莎在跳舞！')
    def daqiu():
        print(boy,'在打球，啦啦啦')
        print(yao,'在抽烟，啦啦啦')  #yao即使没返回，也可以调用，因为对daqiu()函数，yao是外部变量

    #通过return语句和容器数据将局部变量和内部函数返回
    return(girl,boy,tiaowu,daqiu)

#调用内部函数和局部变量


#调用函数获取所有的返回值
result=py02()
#print(result)
nv,nan,tw,dq=result
dq()


#闭包操作2：返回变量和内部函数信息

def demo():
    x=5
    y=6
    def inner1():
        pass
    def inner2():
        pass
    #闭包返回的函数
    def all():
        return(x,y,inner1,inner2)
    return all
#调用函数
bb = demo()
print(bb.__closure__)
'''

#s声明一个lambda表达式

mylamb = lambda x,y:x+y

'''
    相当于以下函数
    def func(x,y):
        return x+y
'''
 
#调用函数
result = mylamb(4,5)
print(result)

#带条件的lambda表达式
mylab = lambda sex:'有胡子' if sex == 'man' else '没胡子'
result=mylab('man')
print(result)



