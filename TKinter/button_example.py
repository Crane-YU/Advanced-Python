import tkinter


# 给button定义的功能
def showLabel():
    global baseFrame
    lb = tkinter.Label(baseFrame, text="LABEL")
    lb.pack()


baseFrame = tkinter.Tk()

btn = tkinter.Button(baseFrame, text="Display", command=showLabel)
btn.pack()

baseFrame.mainloop()