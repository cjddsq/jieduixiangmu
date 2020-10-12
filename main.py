import random
from fractions import Fraction
import prettytable as pt
import tkinter
import pygeoip
import tkinter.messagebox
import sys


# 完成布局
def gui_arrang():
    subjectnum.pack()
    limits.pack()
    display_info.pack()
    result_button.pack()


#把假分数转化为真分数,传进来的是一个分数
def while_1(f):

    rjg = [0, 0]
    rjg[0] = f
    #考虑f为零的情况
    if f == 0:
        return 0
    elif f != 0:
        while rjg[0] >= 1:
            rjg[0] -= 1
            rjg[1] = rjg[1] + 1
        #考虑f为零的情况
        if rjg[1] == 0 or rjg[0] == 0:
            if rjg[1] == 0 and rjg[0] != 0:
                return str(rjg[0])
            if rjg[1] != 0 and rjg[0] == 0:
                return str(rjg[1])
        elif rjg[1] != 0 and rjg[0] != 0:
            return str(rjg[1]) + '\'' + str(rjg[0])


#将中缀表达式转化为后缀表达式
def generate_postfix(list_1):
    # print('算式',infix)
    op_rank = {'×': 2, '÷': 2, '＋': 1, '－': 1}  # 定义加减乘除的优先级
    stack = []  # 用list模拟栈的后进先出
    post_list = []
    for s in list_1:
        s = str(s)
        if s in '＋-－×÷':  # operator
            # 栈不为空，且栈顶运算符的优先级高于当前运算符
            while stack and op_rank.get(
                    stack[-1]) >= op_rank.get(s):  # priority
                post_list.append(stack.pop())
            stack.append(s)
        else:  # operand
            post_list.append(s)
    while stack:
        post_list.append(stack.pop())

    return post_list


#计算后缀表示式
def calculate_postfix(list_1):
    h = 0
    stack = []  # 用list模拟栈的后进先出
    for p in list_1:
        p = str(p)
        if p in '＋－×÷':  # operator

            value_2 = Fraction(stack.pop())  # 第二个操作数
            value_1 = Fraction(stack.pop())  # 第一个操作数

            if p == '＋':
                result = value_1 + value_2
            elif p == '－':
                result = value_1 - value_2
            elif p == '×':
                result = value_1 * value_2
            else:  # 整除
                result = Fraction(value_1, value_2)
                h = 1
            stack.append(result)
        else:
            stack.append(p)
    return stack.pop()


#两个整数操作数
def createInt(tb):

    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    #其实这里已经保证了除数不可能为零
    n1 = random.randint(1, limits_1)
    n2 = random.randint(1, limits_1)
    rjg = 0
    if fh == 0:
        rjg = n1 + n2
    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 - n2
    elif fh == 2:
        rjg = n1 * n2
    elif fh == 3:
        rjg = Fraction(n1, n2)
        #只有这个是分数的形式，所以转化这个就可以了
        rjg = while_1(rjg)
    tb.add_row([n0, n1, opr[fh], n2, ' ', ' ', '='])
    return rjg


#两个带分数
def createFra(tb):

    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    t1 = random.randint(1, limits_1)
    t2 = random.randint(1, limits_1)
    n1 = Fraction(t1, t2)
    t1 = random.randint(1, limits_1)
    t2 = random.randint(1, limits_1)
    n2 = Fraction(t1, t2)
    n1_1 = 0
    n2_1 = 0
    rjg = 0
    anwser = 0
    if fh == 0:
        rjg = n1 + n2
    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 - n2
    elif fh == 2:
        rjg = n1 * n2
    elif fh == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 / n2
    tb.add_row([n0, while_1(n1), opr[fh], while_1(n2), ' ', ' ', '='])
    return while_1(rjg)


#三个整数的
def create_Int():
    a_1 = random.randint(1, limits_1)
    a_2 = random.randint(1, limits_1)
    a_3 = random.randint(1, limits_1)
    f = [0]
    x_1 = random.randint(0, 3)
    if x_1 == 0:
        opr_1 = '＋'
    elif x_1 == 1:
        opr_1 = '－'
    elif x_1 == 2:
        opr_1 = '×'
    elif x_1 == 3:
        opr_1 = '÷'
    x_2 = random.randint(0, 3)
    if x_2 == 0:
        opr_2 = '＋'
    elif x_2 == 1:
        opr_2 = '－'
    elif x_2 == 2:
        opr_2 = '×'
    elif x_2 == 3:
        opr_2 = '÷'
    list_1=[str(a_1),str(opr_1),str(a_2),(opr_2),str(a_3)]
    f = generate_postfix(list_1)
    f[0]=calculate_postfix(f)
    #如果是负数就不把它打印出来
    if f[0] >= 0:
        tb.add_row([
            n0,
            a_1,
            opr_1,
            a_2,
            opr_2,
            a_3,
            '=',
        ])
    return f[0]


#三个带分数的
def create_Fra():
    f_1 = 0
    a_1 = random.randint(1, limits_1)
    a_2 = random.randint(1, limits_1)
    a_3 = random.randint(1, limits_1)
    a_4 = random.randint(1, limits_1)
    a_5 = random.randint(1, limits_1)
    a_6 = random.randint(1, limits_1)
    x_1 = random.randint(0, 3)
    if x_1 == 0:
        opr_1 = '＋'
    elif x_1 == 1:
        opr_1 = '－'
    elif x_1 == 2:
        opr_1 = '×'
    elif x_1 == 3:
        opr_1 = '÷'
    x_2 = random.randint(0, 3)
    if x_2 == 0:
        opr_2 = '＋'
    elif x_2 == 1:
        opr_2 = '－'
    elif x_2 == 2:
        opr_2 = '×'
    elif x_2 == 3:
        opr_2 = '÷'
    list_1 = [
        Fraction(a_1, a_4),
        str(opr_1),
        Fraction(a_2, a_5), (opr_2),
        Fraction(a_3, a_6)
    ]
    f = generate_postfix(list_1)
    f_1 = calculate_postfix(f)
    if f_1 >= 0:
        tb.add_row([
            n0,
            while_1(Fraction(a_1, a_4)),
            str(opr_1),
            while_1(Fraction(a_2, a_5)),
            str(opr_2),
            while_1(Fraction(a_3, a_6)), '='
        ])
    return f_1


#输出的
def newtest():
    opr = ['＋', '－', '×', '÷']
    global n, limits_1
    n = 0
    n = int(subjectnum.get())
    limits_1 = int(limits.get()) - 1
    rjg = []
    rjg_1 = [0]
    rjg_2 = []
    m = 0
    global n0
    n0 = 1
    while m <= (n - 1):
        fh = random.randint(0, 3)
        if fh == 0:
            rjg_1 = createFra(tb)
            n0 = n0 + 1
            rjg.append(rjg_1)
            m = m + 1
        elif fh == 1:
            rjg_1 = createInt(tb)
            n0 = n0 + 1
            rjg.append(rjg_1)
            m = m + 1
        elif fh == 2:
            rjg_1 = create_Int()
            #保证为正数
            while rjg_1 < 0:
                rjg_1 = create_Int()
            n0 = n0 + 1
            rjg_1 = while_1(rjg_1)
            rjg.append(rjg_1)
            m = m + 1
        elif fh == 3:
            rjg_1 = create_Fra()
            #保证为正数
            while rjg_1 < 0:
                rjg_1 = create_Fra()
            n0 = n0 + 1
            #转化为带分数
            rjg_1 = while_1(rjg_1)
            rjg.append(rjg_1)
            m = m + 1
    print(tb)
    m = 0
    while m <= (n - 1):
        tb0.add_row([m + 1, rjg[m]])
        m = m + 1
    print(tb0)


def main_1():
    #定义全局变量
    global tb, tb0
    tb = pt.PrettyTable()
    tb.field_names = ["题号", "操作数1", "运算符1", "操作数2", "运算符2", "操作数3", "  "]
    tb0 = pt.PrettyTable()
    tb0.field_names = ["题号", "答案"]
    newtest()
    # 为回显列表赋值
    #*****************************************************************************************************
    a__2 = 0
    for item in str(tb0).split('\n'):

        display_info.insert(a__2, item)
        a__2 = a__2 + 1
    a__2 = 0
    for item in str(tb).split('\n'):
        display_info.insert(a__2, item)
        a__2 = a__2 + 1
    okqqq()
    if result:
        txt1 = open("C:/Users/Administrator.USER-20190905VU/Desktop/四则运算/Exercises.txt", "w")
        txt1.write(
            str(tb) + '\n' +
            '**************************************************************************************************'
            + '\n')
        txt1.close()
        txt2 = open("C:/Users/Administrator.USER-20190905VU/Desktop/四则运算/Answers.txt", "w")
        txt2.write(
            str(tb0) + '\n' +
            '**************************************************************************************************'
            + '\n')
        txt2.close()
    else:
        txt1 = open("C:/Users/Administrator.USER-20190905VU/Desktop/四则运算/Exercises.txt", "a")
        txt1.write(
            str(tb) + '\n' +
            '**************************************************************************************************'
            + '\n')
        txt1.close()
        txt2 = open("C:/Users/Administrator.USER-20190905VU/Desktop/四则运算/Answers.txt", "a")
        txt2.write(
            str(tb0) + '\n' +
            '**************************************************************************************************'
            + '\n')
        txt2.close()
    #print('是否继续做题yes/no')
    okqqq_2()
    y = input()
    if y == result:

        main_1()




def main():
    gui_arrang()
    tkinter.mainloop()
    pass

root = tkinter.Tk()
# 给主窗口设置标题内容
root.title("四则运算,第一个框是生成数量，第二个框是生成范围")
# 创建一个输入框,并设置尺寸
subjectnum = tkinter.Entry(root, width=10)
limits = tkinter.Entry(root, width=10)
# 创建一个回显列表
display_info = tkinter.Listbox(root, width=100, height=20)
# 创建一个查询结果的按钮
result_button = tkinter.Button(root, command=main_1, text="生成")


def okqqq():
    # 弹出对话框
    global result
    result = tkinter.messagebox.askokcancel(title='标题~', message='是否覆盖原文件')


    # 返回值为True或者False
def okqqq_2():
    # 弹出对话框
    global result
    result = tkinter.messagebox.askokcancel(title='标题~', message='是否继续做题')
    # 返回值为True或者False



#执行主函数
main()
