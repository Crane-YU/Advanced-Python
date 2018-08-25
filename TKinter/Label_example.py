import tkinter

base = tkinter.Tk()
base.wm_title("Label Test")

# Could support many labels with defined parameter
lb1 = tkinter.Label(base, text="Python AI")
lb1.pack()

lb2 = tkinter.Label(base, text="Green background", background="green")
lb2.pack()

lb3 = tkinter.Label(base, text="Blue background", background="blue")
lb3.pack()

base.mainloop()
