#�հ�����1
'''
def py02():
    #�ֲ�����
    girl='��ɯɯ'
    boy='�߲�'
    yao='����'

    #�ڲ�����
    def tiaowu():
        print('��ɯɯ�����裡')
    def daqiu():
        print(boy,'�ڴ���������')
        print(yao,'�ڳ��̣�������')  #yao��ʹû���أ�Ҳ���Ե��ã���Ϊ��daqiu()������yao���ⲿ����

    #ͨ��return�����������ݽ��ֲ��������ڲ���������
    return(girl,boy,tiaowu,daqiu)

#�����ڲ������;ֲ�����


#���ú�����ȡ���еķ���ֵ
result=py02()
#print(result)
nv,nan,tw,dq=result
dq()


#�հ�����2�����ر������ڲ�������Ϣ

def demo():
    x=5
    y=6
    def inner1():
        pass
    def inner2():
        pass
    #�հ����صĺ���
    def all():
        return(x,y,inner1,inner2)
    return all
#���ú���
bb = demo()
print(bb.__closure__)
'''

#s����һ��lambda���ʽ

mylamb = lambda x,y:x+y

'''
    �൱�����º���
    def func(x,y):
        return x+y
'''
 
#���ú���
result = mylamb(4,5)
print(result)

#��������lambda���ʽ
mylab = lambda sex:'�к���' if sex == 'man' else 'û����'
result=mylab('man')
print(result)



