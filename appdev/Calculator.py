import tkinter

root = tkinter.Tk()
root.title("Calculator")
L1 = tkinter.Label(root,text="Enter number 1 : ")
L1.pack(side = tkinter.LEFT)
E1 = tkinter.Entry(root, bd = 5)
E1.pack(side = tkinter.RIGHT)

root.mainloop()