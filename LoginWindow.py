import tkinter as tk
import mysql.connector
import bcrypt


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbactivity4"
)
cursor = conn.cursor()
root =tk.Tk()

frame = tk.Frame(root,width=400,height=200)
#---Label
title=tk.Label(root,  text="Login System", font=('Arial',20,'bold'))
title.place(x=100,y=0)

unamelbl=tk.Label(root,  text="Username", font=('Arial',14))
unamelbl.place(x=25,y=50)

passWlbl=tk.Label(root,  text="Password", font=('Arial',14))
passWlbl.place(x=25,y=100)

regLnklbl=tk.Label(root,  text="Register Here", font=('Arial',10), fg="blue")
regLnklbl.place(x=275,y=130)

succLabel=tk.Label(root,  text="", font=('Arial',12))
succLabel.place(x=150,y=175)
#---Label


#--Fields
unameInp = tk.Entry(root, width=30)
unameInp.place(x=125,y=55)

passInp = tk.Entry(root, show='*',width=30)
passInp.place(x=125,y=105)
#--Fields

#--Button
submitBtn= tk.Button(root,text="Login", width=15)
submitBtn.place(x=150, y=130)
#--Button
frame.pack()



#--backend
def switch_to_second_window(event):  
    root.withdraw() 
    import Register
    Register.root.deiconify()
    
regLnklbl.bind('<Button-1>',switch_to_second_window)



def loginAcc():
    userName=unameInp.get()
    print(userName)
    sql = "SELECT * FROM `tblusers` WHERE `username` = %s"
    cursor.execute(sql,(userName,))
    row=cursor.fetchone()
    print(row is not None)
    if row is not None:  
        print(row[1].encode('utf-8'))

        if(bcrypt.checkpw(passInp.get().encode('utf-8'),row[1].encode('utf-8'))):
            print(row[0])
            print(row[1])
            print(row[2])
            unameInp.delete(0, tk.END)
            passInp.delete(0, tk.END)
            succLabel.config(text="Authorized Access", fg='green')
            import Open
            root.withdraw()
            Open.root.deiconify()
        else:
            succLabel.config(text="Invalid user input", fg='red')
    else:
        succLabel.config(text="Invalid user input", fg='red')
    
        
submitBtn.config(command=loginAcc)











root.resizable(False,False)
root.mainloop()