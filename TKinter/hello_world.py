import tkinter

base = tkinter.Tk()

# 负责标题
base.wm_title("Label Test")

# 创建一个label
lb = tkinter.Label(base, text="Python Label")

# 给相应组件指定布局
lb.pack()

# 消息循环
base.mainloop()
