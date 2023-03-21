from tkinter import *
import os
from StudTheme import Stud, Theme

root=Tk()
l1=Listbox(root,width=30,height=15,font="Arial 27")
b1=Button(text="Add Stud", font="Arial 27")
e1=Entry(width=30,font="Arial 27")
spisFStud=os.listdir("StudTheme/Stud")
print(spisFStud)
stud=[]
for i in spisFStud:
    f=open(f"StudTheme/Stud/{i}","r")
    s=f.readlines()
    ob=Stud(s[0])

    if len(s)==2:
        ob.setSpisOtm(s[1].split())
    stud.append(ob)
    l1.insert(END,ob.fio)
    f.close()

def addStud(event): #ДОБАВЛЕНИЕ ЗАПИСИ STUD
    fio=e1.get()
    if len(fio)!=0:
        ob=Stud(fio)
        stud.append(ob)
        l1.insert(END,ob.fio)
        f=open(f"StudTheme/Stud/{ob.fio}","w")
        f.write(ob.fio+"\n")
        f.close()
        e1.delete(0,END)
    else:
        e1.insert(0,"")
b1.bind("<Button-1>",addStud)
def l1f(event):                 #Add list2 for Stud
    s=list(l1.curselection())
    #l1.get(s[0])
    print(s[0])
    pr=""
    for i in stud:
       if l1.get(s[0])==i.fio:
        pr=i
        break
    root1=Tk()
    e11=Entry(root1,width=30,font="Arial 27")
    e12=Entry(root1,width=30,font="Arial 27")
    b12=Button(root1,text="Add",width=30,font="Arial 27")
    e11.insert(0,pr.fio)
    print(pr.spisOtm)
    e12.insert(0," ".join(pr.spisOtm))
    def b12f(event,pr):
        pr.setSpisOtm(e12.get().split())
        print(pr.getSpisOtm())
        mas=os.listdir("StudTheme/Stud")
        for i in mas:
            if pr.getFio()[:-1]==i:
                f=open(f"StudTheme/Stud/{i}","w")
                f.write(pr.getFio()+" ".join(pr.getSpisOtm()))
                f.close()
                break

    b12.bind("<Button-1>",lambda event,f=pr: b12f(event,f))
    e11.pack()
    e12.pack()
    b12.pack()
    root1.mainloop()
l1.bind("<Double-Button-1>",l1f)
l1.pack()
b1.pack()
e1.pack()
root.mainloop()