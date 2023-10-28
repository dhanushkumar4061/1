from tkinter import *
mw=Tk()
# user_input=Entry(mw,text="vidya varadhi",pady20,font=("Cooper Black"),20)
# user_input.pack(pady=18)
mw.iconbitmap("images/insta35.ico")
mw.title("black insta")
label1=Label(mw,text="vidya varsdhi",font=("Cooper Black",20),fg="green")
label2=Label(mw,text="vidya varsdhi",font=("Cooper Black",20),fg="green")
but=Button(mw,text="click me",font=("Cooper Black",20),fg="white",bg="#13fc03")
label1.grid(row=0,column=1)
label2.grid(row=1,column=2)
but.grid(row=1,column=1,pady=30)

mw.mainloop()