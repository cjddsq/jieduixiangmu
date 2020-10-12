import random
from fractions import Fraction
import prettytable as pt
import tkinter
import pygeoip
import tkinter.messagebox
import re


# 完成布局

def cut_text(text,lenth):
    textArr = re.findall('.{'+str(lenth)+'}', text)
    textArr.append(text[(len(textArr)*lenth):])

def duibi():
    
    #打开抄袭论文文本
    cnt_0=0
    list_1000=[]
    list_1=[]
    list_2=[]
    list_3=[]
    
    cnt=0
    s=[]
    s=[]
    s_3=[0,0]
    s_4=[]
    s_1=0
    cnt_1=0
    cnt_2=0
    cnt_3=0
    cnt_4=0
    cnt_5=0
    cnt_6=0
    cnt_7=0
    str_1000=''
    a_9=0
    URL=str()
    URL="C:/Users/陈乙鑫/Desktop/题目.txt"
    book_b0=open(URL,'r',encoding='gbk')
    book_b0=book_b0.read()
    
    book_b0=book_b0.replace('算式','')
    book_b0=book_b0.replace(' ','')
    book_b0=book_b0.replace('*','')
    book_b0=book_b0.replace('-','')
    book_b0=book_b0.replace('+','')
    book_b0=book_b0.replace('|题号||','')
    book_b0=book_b0.replace('\n','')
    book_b0=book_b0.replace('||','|')
    
    for item_1 in book_b0.split('|'):
        cnt_0=cnt_0+1
        if cnt_0%2==1:
            list_1.append(item_1)
    del list_1[0]
    
    for item_2 in list_1:
        s=0
        s_3=[0,0]
        cnt_7=0
       
        ##################
        list_3=[]
        for item_6 in item_2:
            if item_6 in '[＋,－,×,÷]':
                list_3.append(item_6)

        
        
        s=re.split('[＋,－,×,÷,\']', item_2)
        
        
        cnt_1=0
        for item_3 in s:
            cnt_1=cnt_1+1
            if len(item_3)>2:
            
                s_3=s[cnt_1-1].split('/')
               
                s[cnt_1-1]=str(Fraction(s[cnt_1-1])+Fraction(s[cnt_1-2]))
               
        for item_4 in s:
            if len(item_4)>2:
                s_4.append(item_4)
        
        list_4=[]
        cnt_3=0
        for item_5 in s:
            cnt_3=cnt_3+1
            if len(item_5)>2:
                list_4.append(cnt_3-1)
        
        for item_7 in list_4:
          
            if cnt_7==0:
                break
            s[item_7]=s_4[cnt_7-1]
            cnt_7=cnt_7+1
        
        a_9=0
        for item_7 in list_4:

            del s[item_7-1-a_9]
            a_9=a_9+1
         
        cnt_5=min(len(s),len(list_3))
        str_1000=''
        cnt_6=0
        while(cnt_6<cnt_5):
            str_1000=str_1000+str(s[cnt_6])+list_3[cnt_6]
            cnt_6=cnt_6+1
            
   
        
        if len(s)>len(list_3):
            str_1000=str_1000+str(s[cnt_6])
        elif len(s)<len(list_3):
            str_1000=str_1000+list_3[cnt_6]
        list_1000.append(str_1000)
    return list_1000

def duibi_1():
    
    #打开抄袭论文文本
    cnt_0=0
    list_1=[]
    list_2=[]
    list_3=[]
    list_1000=[]
    
    cnt=0
    s=[]
    s=[]
    s_3=[0,0]
    s_4=[]
    s_1=0
    cnt_1=0
    cnt_2=0
    cnt_3=0
    cnt_4=0
    cnt_5=0
    cnt_6=0
    cnt_7=0
    str_1000=''
    a_9=0
    URL=str()
    URL="C:/Users/陈乙鑫/Desktop/答案.txt"
    book_b0=open(URL,'r',encoding='gbk')
    book_b0=book_b0.read()
    
    book_b0=book_b0.replace('答案','')
    book_b0=book_b0.replace(' ','')
    book_b0=book_b0.replace('*','')
    book_b0=book_b0.replace('-','')
    book_b0=book_b0.replace('+','')
    book_b0=book_b0.replace('|题号||','')
    book_b0=book_b0.replace('\n','')
    book_b0=book_b0.replace('||','|')
    
    for item_1 in book_b0.split('|'):
        cnt_0=cnt_0+1
        if cnt_0%2==1:
            list_1.append(item_1)
    del list_1[0]
    
    for item_2 in list_1:
        s=0
        s_3=[0,0]
        cnt_7=0
       
        ##################
        list_3=[]
        for item_6 in item_2:
            if item_6 in '[＋,－,×,÷]':
                list_3.append(item_6)

        list_1000.append(item_2)
    
    return list_1000

def du():

    list_1000=[]
    list_2000=[]
    list_3000=[]
    list_5000=[]
    list_6000=[]
    list_1000=duibi()
    list_2000=duibi_1()

    for str_1000 in list_1000:
        list_3000=re.split(r'([＋,－,×,÷])',str_1000)
       
    
        list_5000.append(while_1(calculate_postfix(generate_postfix(list_3000))))
    
    a_1=len(list_5000)
 
    list_6000=[]
    while a_1:
        if list_5000[a_1-1]==list_2000[a_1-1]:
            list_6000.append(str(1))
        else:
            list_6000.append(str(0))
        a_1=a_1-1
    print('list_6000',list_6000)
    return list_6000
    list_5000=[]
def gui_arrang():
    ip_input.pack()
    ip_input_2.pack()
    display_info.pack()
    display_info_1.pack()
    result_button.pack()
    result_button_1.pack()
    


#把假分数转化为真分数,传进来的是一个分数
def while_1(f):
    
    rjg = [0,0]
    rjg[0] = f
    #考虑f为零的情况
    if f==0:
        return 0
    
    while rjg[0]>=1:
        rjg[0]-=1
        rjg[1]=rjg[1]+1
       #考虑f为零的情况
    if rjg[1] == 0 or rjg[0] == 0:
        if rjg[1] == 0 and rjg[0] != 0:
            return str(rjg[1])+'\''+str(rjg[0])
        if rjg[1] != 0 and rjg[0] == 0:
            return str(rjg[1])
    elif rjg[1] != 0 and rjg[0] != 0:
        return str(rjg[1])+'\''+str(rjg[0])
        
#将中缀表达式转化为后缀表达式
def generate_postfix(list_1):
      
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
                    #h=1

                stack.append(result)
            else:
                stack.append(p)
      
        return stack.pop()

#两个整数操作数
def newint(tb):
    #global n_x
    #n_x=10
    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    #其实这里已经保证了除数不可能为零
    n1 = random.randint(1,n_x)
    n2 = random.randint(1,n_x)
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
   
    tb.add_row([str(n0),str(n1)+opr[fh]+str(n2)])
    return rjg
    
#两个带分数
def newfra(tb):
     
   
    
    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    t1 = random.randint(1,n_x)
    t2 = random.randint(1,n_x)
    n1 = Fraction(t1, t2)
    t1 = random.randint(1,n_x)
    t2 = random.randint(1,n_x)
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
    tb.add_row([str(n0),str(while_1(n1))+opr[fh]+str(while_1(n2))])

    #return rjg
    return while_1(rjg)
#三个整数的
def new_int():
    a_1=random.randint(1, n_x)
    a_2=random.randint(1, n_x)
    a_3=random.randint(1, n_x)
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
    list_1=[str(a_1),str(opr_1),str(a_2),(opr_2),str(a_3)]
    #f[0] =generate_postfix(str(a_1)+str(opr_1)+str(a_2)+str(opr_2)+str(a_3))
    f = generate_postfix(list_1)
    #tb.add_row([n0,a_1,opr_1,a_2,opr_2,a_3,'=',])
 
    f[0]=calculate_postfix(f)

    #如果是负数就不把它打印出来
    if f[0] >= 0:
        tb.add_row([str(n0),str(a_1)+opr_1+str(a_2)+opr_2+str(a_3)])
    return f[0]

#三个带分数的
def new_fra():
    f_1= 0
    a_1=random.randint(1, n_x)
    a_2=random.randint(1, n_x)
    a_3=random.randint(1, n_x)
    a_4=random.randint(1, n_x)
    a_5=random.randint(1, n_x)
    a_6=random.randint(1, n_x)
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

    if f_1 >= 0:
        tb.add_row([str(n0),str(while_1(Fraction(a_1, a_4)))+str(opr_1)+str(while_1(Fraction(a_2, a_5)))+str(opr_2)+str(while_1(Fraction(a_3, a_6)))])
    return f_1


#输出的
def newtest():
    opr = ['＋', '－', '×', '÷']
   
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
    
        if fh==0:
            rjg_1=newfra(tb)
            n0=n0+1
            rjg.append(rjg_1)
            #rjg.append(rjg_1[0])
            #要与三个操作数的相配合
            #rjg_2.append(rjg_1)
            m=m+1
        elif fh==1:
          
            rjg_1=newint(tb)
            n0=n0+1
            rjg.append(rjg_1)
            #要与三个操作数的相配合
            #rjg_2.append(rjg_1)
       
            m=m+1
        elif fh==2:
            rjg_1=new_int()
          
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
           
          
  

    m=0
    while m<=(n-1):
        #因为两个操作数和三个操作数不同，所以要分开来
        #if fh == 2 or fh==3:
            #tb0.add_row([m+1,str(rjg_2[m])+'\''+str(rjg[m])])
        #elif fh == 0 or fh == 1:
            #tb0.add_row([m+1,rjg[m]])
        tb0.add_row([m+1,rjg[m]])
        m=m+1
 




def main_1():
    #定义全局变量
    global tb, tb0,n_x,list_10000
    list_10000=[]
    #n_x=20
    n_x=int(ip_input_2.get())
    tb = pt.PrettyTable()
    tb.field_names = ["题号","算式"]
    tb0 = pt.PrettyTable()
    tb0.field_names = ["题号","答案"]
    newtest()
    # 为回显列表赋值
    
    a__2=0
    #########3list_10000
    a__2=0
    
    
    for item in str(tb0).split('\n'):
            
        display_info.insert(a__2,item)
        a__2=a__2+1
    a__2=0
    for item in str(tb).split('\n'):
        display_info.insert(a__2,item)
        a__2=a__2+1
    '''for item in str(tb).split('\n'):
        display_info.insert(a__2,item)
        a__2=a__2+1'''
    
            
  
    #弹出窗
    okqqq()
  
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
def main_2():
    
    list_10000=du()
    print(list_10000)
    # 为回显列表赋值
    
    
    
    
    
    
   
    display_info_1.insert(0,list_10000)
 
   
   
    
    
    
    
    
    
    
    




def main():

    gui_arrang()
    tkinter.mainloop()
    pass
root = tkinter.Tk()
        # 给主窗口设置标题内容
root.title("四则运算")
        # 创建一个输入框,并设置尺寸
ip_input =tkinter.Entry(root,width=10)
ip_input_2 =tkinter.Entry(root,width=10)

        # 创建一个回显列表
display_info = tkinter.Listbox(root,width=100,height=20)
display_info_1 = tkinter.Listbox(root,width=100,height=5)
        # 创建一个查询结果的按钮
result_button = tkinter.Button(root, command = main_2, text = "校验")
result_button_1 = tkinter.Button(root, command = main_1, text = "生成")
def okqqq():
    # 弹出对话框
    global result
    result = tkinter.messagebox.askokcancel(title = '标题~',message='是否覆盖原文件')
    # 返回值为True或者False


    

main()




        
            




   
                
                




       





                    
    
                 





        
    

        

#duibi()
def du():

    list_1000=[]
    list_2000=[]
    list_3000=[]
    list_5000=[]
    list_6000=[]
    list_1000=duibi()
    list_2000=duibi_1()
  
    for str_1000 in list_1000:
        list_3000=re.split(r'([＋,－,×,÷])',str_1000)
      
    
        list_5000.append(while_1(calculate_postfix(generate_postfix(list_3000))))
  
    a_1=len(list_5000)
 
    list_6000=[]
    while a_1:
        if list_5000[a_1-1]==list_2000[a_1-1]:
            list_6000.append(str(1))
        else:
            list_6000.append(str(0))
        a_1=a_1-1
    
    return list_6000.reverse
    list_5000=[]

#执行主函数














