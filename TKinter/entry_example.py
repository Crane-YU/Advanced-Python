# 输入框案例
import tkinter


# 模拟的是登录函数
def reg():
    # 从相应输入框中得到用户的输入
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    if name == "111" and pwd == "222":
        # 赋值给lb3
        lb3["text"] = "登录成功"
    else:
        lb3["text"] = "用户名或密码错误"
        # 输入框删除掉用户输入的内容
        # 注意delete的两个参数，表示从第几个删除到第几个
        e1.delete(0, t1)
        e2.delete(0, t2)


# 创建baseFrame
baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame, text="用户名")
lb1.grid(row=0, column=0, stick=tkinter.W)

lb2 = tkinter.Label(baseFrame, text="密码: ")
lb2.grid(row=1, column=0, stick=tkinter.W)

# 创建输入框
e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, stick=tkinter.E)

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, stick=tkinter.E)
e2['show'] = '*'

# command：当按钮被点击后启动相应的处理函数
btn = tkinter.Button(baseFrame, text="登录", command=reg)
btn.grid(row=2, column=1, stick=tkinter.S)

lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row=3)

# 启动baseFrame
baseFrame.mainloop()
