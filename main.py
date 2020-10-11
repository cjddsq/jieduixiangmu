import random
from fractions import Fraction
import prettytable as pt
import tkinter
import pygeoip
import tkinter.messagebox


# 完成布局
def gui_arrang():
    ip_input.pack()
    display_info.pack()
    result_button.pack()
    


#把假分数转化为真分数,传进来的是一个分数
def while_1(f):
    
    rjg = [0,0]
    rjg[0] = f
    #考虑f为零的情况
    if f == 0:
        return 0
    elif f != 0: 
        while rjg[0]>=1:
            rjg[0]-=1
            rjg[1]=rjg[1]+1
        #考虑f为零的情况
        if rjg[1] == 0 or rjg[0] == 0:
            if rjg[1] == 0 and rjg[0] != 0:
                return str(rjg[0])
            if rjg[1] != 0 and rjg[0] == 0:
                return str(rjg[1])
        elif rjg[1] != 0 and rjg[0] != 0:
            return str(rjg[1])+'\''+str(rjg[0])

#将中缀表达式转化为后缀表达式
def generate_postfix(list_1):
       # print('算式',infix)
        op_rank = {'×': 2, '÷': 2, '＋': 1, '－': 1}  # 定义加减乘除的优先级
        stack = []  # 用list模拟栈的后进先出
        post_list = []
        for s in list_1:
            s=str(s)
            if s in '＋-－×÷':  # operator
                # 栈不为空，且栈顶运算符的优先级高于当前运算符
                while stack and op_rank.get(stack[-1]) >= op_rank.get(s):  # priority
                    post_list.append(stack.pop())
                stack.append(s)
            else:  # operand
                post_list.append(s)
        while stack:
            post_list.append(stack.pop())
        
        return post_list
#计算后缀表示式
def calculate_postfix(list_1):
        """
        calculate postfix expression
        :param postfix: postfix expression str, like '23x83/+'
        :return: int result, like 2x3+8/3=6+2=8
        """
        h=0
        stack = []  # 用list模拟栈的后进先出

        for p in list_1:
            p=str(p)
            if p in '＋－×÷':  # operator
          
                value_2 = Fraction(stack.pop ())  # 第二个操作数
                value_1 = Fraction(stack.pop())  # 第一个操作数
               
                if p == '＋':
                    result = value_1 + value_2
                elif p == '－':
                    result = value_1 - value_2
                elif p == '×':
                    result = value_1 * value_2
                else:   # 整除
                    result = Fraction(value_1,value_2)
                    h=1

                stack.append(result)
            else:
                stack.append(p)
       # print('stack:',stack,'\n','p:',p)
        return stack.pop()

#两个整数操作数
def newint(tb):
   
    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    #其实这里已经保证了除数不可能为零
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    rjg = 0
    if fh == 0:
        rjg = n1 + n2
    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 - n2
    elif fh == 2:
        rjg = n1 * n2
    elif fh == 3:
        #n1, n2 = max(n1, n2), min(n1, n2)
        #while n1 % n2 != 0:
            #n1 = random.randint(1, 10)
            #n2 = random.randint(1, 10)
            #n1, n2 = max(n1, n2), min(n1, n2)
        #rjg = int(n1 / n2)
        rjg = Fraction(n1, n2)
        #只有这个是分数的形式，所以转化这个就可以了
        rjg = while_1(rjg)
    #print(n1, opr[fh], n2, '= ', end='')
    #print(str(0),opr[fh],str(0),'=')
    tb.add_row([n0,n1,opr[fh],n2,' ',' ','='])
    return rjg
    
#两个带分数
def newfra(tb):
     
   
    
    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    t1 = random.randint(1, 10)
    t2 = random.randint(1, 10)
    n1 = Fraction(t1, t2)
    t1 = random.randint(1, 10)
    t2 = random.randint(1, 10)
    n2 = Fraction(t1, t2)
    n1_1=0
    n2_1=0
    #rjg = [0,0]
    rjg = 0
    anwser=0
    if fh == 0:
        #rjg[0]=n1 + n2
        rjg = n1 + n2
        #while rjg[0]>=1:
            #rjg[0]-=1
            #rjg[1]=rjg[1]+1


    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        #rjg[0]=n1 - n2
        rjg = n1 - n2
        #print(rjg[0])
       # while rjg[0]>=1:
            #rjg[0]-=1
           # rjg[1]=rjg[1]+1
    elif fh == 2:
        #rjg[0] = n1 * n2
        rjg = n1 * n2
        #while rjg[0]>=1:
           #rjg[0]-=1
           #rjg[1]=rjg[1]+1
    elif fh == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        #rjg[0] = n1 / n2
        rjg = n1 / n2
        #while rjg[0]>=1:
          # rjg[0]-=1
          # rjg[1]=rjg[1]+1
    #while n1>=1:
            #n1-=1
            #n1_1=n1_1+1 
    #while n2>=1:
            #n2-=1
            #n2_1=n2_1+1
    
    #tb.add_row([n0,str(n1_1)+'\''+str(n1),opr[fh],str(n2_1)+'\''+str(n2),'','','='])
    tb.add_row([n0,while_1(n1),opr[fh],while_1(n2),' ',' ','='])
    #print('\t',n1_1,'\'',n1,'\t',opr[fh],'\t', n2_1,'\'',n2,'\t','= ', end='')
    #return rjg
    return while_1(rjg)
#三个整数的
def new_int():
    a_1=random.randint(1, 9)
    a_2=random.randint(1, 9)
    a_3=random.randint(1, 9)
    f = [0]
    #opr = ['＋', '－', '×', '÷']
    x_1=random.randint(0, 3)
    if x_1==0:
        opr_1='＋'
    elif x_1==1:
        opr_1='－'
    elif x_1==2:
        opr_1='×'
    elif x_1==3:
        opr_1='÷'
    x_2=random.randint(0, 3)
    if x_2==0:
        opr_2='＋'
    elif x_2==1:
        opr_2='－'
    elif x_2==2:
        opr_2='×'
    elif x_2==3:
        opr_2='÷'
    f[0] =generate_postfix(str(a_1)+str(opr_1)+str(a_2)+str(opr_2)+str(a_3))
    #tb.add_row([n0,a_1,opr_1,a_2,opr_2,a_3,'=',])
    #print("算式",str(a_1)+str(opr_1)+str(a_2)+str(opr_2)+str(a_3))
    #print(f[0])
    f[0]=calculate_postfix(f[0])
    #print(f)
    #print(f)
    #如果是负数就不把它打印出来
    if f[0] >= 0:
        tb.add_row([n0,a_1,opr_1,a_2,opr_2,a_3,'=',])
    return f[0]

#三个带分数的
def new_fra():
    f_1= 0
    a_1=random.randint(1, 9)
    a_2=random.randint(1, 9)
    a_3=random.randint(1, 9)
    a_4=random.randint(1, 9)
    a_5=random.randint(1, 9)
    a_6=random.randint(1, 9)
    #opr = ['＋', '－', '×', '÷']
    x_1=random.randint(0, 3)
    if x_1==0:
        opr_1='＋'
    elif x_1==1:
        opr_1='－'
    elif x_1==2:
        opr_1='×'
    elif x_1==3:
        opr_1='÷'
    x_2=random.randint(0, 3)
    if x_2==0:
        opr_2='＋'
    elif x_2==1:
        opr_2='－'
    elif x_2==2:
        opr_2='×'
    elif x_2==3:
        opr_2='÷'
    #*******************************************************************************************
    #tb.add_row([n0,while_1(Fraction(a_1, a_4)),str(opr_1),while_1(Fraction(a_2, a_5)),str(opr_2),while_1(Fraction(a_3, a_6)),'='])
    list_1=[Fraction(a_1, a_4),str(opr_1),Fraction(a_2, a_5),(opr_2),Fraction(a_3, a_6)]
    f=generate_postfix(list_1)
    f_1=calculate_postfix(f)
    
    #while int(f_1[0])>=1:
            #f_1[0]-=1
            #f_1[1]+=1
   #print(f_1)
    if f_1 >= 0:
        tb.add_row([n0,while_1(Fraction(a_1, a_4)),str(opr_1),while_1(Fraction(a_2, a_5)),str(opr_2),while_1(Fraction(a_3, a_6)),'='])
    return f_1


#输出的
def newtest():
    opr = ['＋', '－', '×', '÷']
    print('输入题库所需要的题目数量')
    global n
    n=0
    n=int(ip_input.get())
    rjg=[]
    rjg_1=[0]
    rjg_2=[]
    m=0
    global n0
    n0=1
    while m<=(n-1):
        fh=random.randint(0, 3)
        #fh=3
        #print(m+1,end='、')
        if fh==0:
            rjg_1=newfra(tb)
            n0=n0+1
            rjg.append(rjg_1)
            #rjg.append(rjg_1[0])
            #要与三个操作数的相配合
            #rjg_2.append(rjg_1)
            m=m+1
        elif fh==1:
            #print(m+1,end='、')
            rjg_1=newint(tb)
            n0=n0+1
            rjg.append(rjg_1)
            #要与三个操作数的相配合
            #rjg_2.append(rjg_1)
            #print(' ')
            m=m+1
        elif fh==2:
            rjg_1=new_int()
            #print(rjg_1)
            #if rjg_1[0] < 0:
                #rjg_1=new_int()
            #保证为正数
            while rjg_1 < 0:
                rjg_1=new_int()
            n0=n0+1
            #转化为带分数
            #while rjg_1[0]>=1:
               #rjg_1[0]-=1
               #rjg_1[1]=rjg_1[1]+1
            rjg_1 = while_1(rjg_1)
            rjg.append(rjg_1)
            #rjg_2.append(rjg_1[1])
            m=m+1
        elif fh==3:
            rjg_1=new_fra()
            #保证为正数
            while rjg_1 < 0:
                rjg_1=new_fra()
            n0=n0+1
            #转化为带分数
            #while rjg_1[0]>=1:
               #rjg_1[0]-=1
               #rjg_1[1]=rjg_1[1]+1
             #转化为带分数
            rjg_1 = while_1(rjg_1)
            rjg.append(rjg_1)
            #rjg_2.append(rjg_1[1])
            m=m+1
            #print(rjg,'\n',rjg_2)
          
    print(tb)
    #print('答案：')
    #print('*********************************')
    m=0
    while m<=(n-1):
        #因为两个操作数和三个操作数不同，所以要分开来
        #if fh == 2 or fh==3:
            #tb0.add_row([m+1,str(rjg_2[m])+'\''+str(rjg[m])])
        #elif fh == 0 or fh == 1:
            #tb0.add_row([m+1,rjg[m]])
        tb0.add_row([m+1,rjg[m]])
        m=m+1
    print(tb0)




def main_1():
    #定义全局变量
    global tb, tb0
    tb = pt.PrettyTable()
    tb.field_names = ["题号","操作数1","运算符1", "操作数2","运算符2","操作数3","  "]
    tb0 = pt.PrettyTable()
    tb0.field_names = ["题号","答案"]
    newtest()
    # 为回显列表赋值
    #*****************************************************************************************************
    a__2=0
    for item in str(tb0).split('\n'):
            
            display_info.insert(a__2,item)
            a__2=a__2+1
    a__2=0
    for item in str(tb).split('\n'):
            display_info.insert(a__2,item)
            a__2=a__2+1
    #display_info.insert(0,"")=str(tb)
    #print(type(tb))
    #print("是否覆盖原文件yes/no")
    okqqq()
    #s=input()
    if result:
        txt1 = open("C:/Users/陈乙鑫/Desktop/题目.txt", "w")
        txt1.write( str(tb)+'\n'+'**************************************************************************************************'+'\n' )
        txt1.close()
        txt2 = open("C:/Users/陈乙鑫/Desktop/答案.txt", "w")
        txt2.write( str(tb0)+'\n'+'**************************************************************************************************'+'\n' )
        txt2.close()
    else:
        txt1 = open("C:/Users/陈乙鑫/Desktop/题目.txt", "a")
        txt1.write( str(tb)+'\n'+'**************************************************************************************************'+'\n' )
        txt1.close()
        txt2 = open("C:/Users/陈乙鑫/Desktop/答案.txt", "a")
        txt2.write( str(tb0)+'\n'+'**************************************************************************************************'+'\n' )
        txt2.close()
    #print('是否继续做题yes/no')
    okqqq_2()
    y=input()
    if y==result:
        
        main_1()
    

#main()


#**************************************************************************************
#**************************************************************************************
#**************************************************************************************




def main():

    gui_arrang()
    tkinter.mainloop()
    pass
root = tkinter.Tk()
        # 给主窗口设置标题内容
root.title("四则运算")
        # 创建一个输入框,并设置尺寸
ip_input =tkinter.Entry(root,width=10)

        # 创建一个回显列表
display_info = tkinter.Listbox(root,width=100,height=20)

        # 创建一个查询结果的按钮
result_button = tkinter.Button(root, command = main_1, text = "生成")

def okqqq():
    # 弹出对话框
    global result
    result = tkinter.messagebox.askokcancel(title = '标题~',message='是否覆盖原文件')
    # 返回值为True或者False
def okqqq_2():
    # 弹出对话框
    global result
    result = tkinter.messagebox.askokcancel(title = '标题~',message='是否继续做题')
    # 返回值为True或者False
    

main()


    







