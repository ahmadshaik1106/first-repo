from tkinter import*


def convert():
    C = float(Fentry.get())
    F = (C*9/5)+32
    ld["text"]=str(F)
    C = float(Fentry.get())
    K = C+273.15
    ld1["text"]=str(K)
    Fentry.delete(0,END)
    
root = Tk()
root.title("Temperature Converter")
root.geometry("295x120+550+300")

l1=Label(root,text="Enter temperature in C :")
l2=Label(root,text="Temperature in K :")
l3=Label(root,text="Temperature in F :")
ld=Label(root)
ld1=Label(root)
Fentry = Entry(root)

btn=Button(root,width=10,text="Convert",command=convert)
btn2=Button(root,width=10,text="close",command=root.destroy)

l1.grid(row=0,column=0)
Fentry.grid(row=0,column=1)
l2.grid(row=1,column=0,sticky=W)
l3.grid(row=2,column=0,sticky=W)
ld.grid(row=2,column=1,sticky=W)
ld1.grid(row=1,column=1,sticky=W)
btn.grid(row=3,column=1,sticky=E)
btn2.grid(row=4,column=1,sticky=E)
root.mainloop()
