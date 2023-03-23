import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbactivity4"
)

    


cursor = conn.cursor()

root = tk.Tk()

welcome= tk.Label(root, text="Dashboard")
welcome.grid(row=0, column=0, sticky="W")


logoutlbl=tk.Label(root,  text="Logout", font=('Arial',10), fg="blue")
logoutlbl.grid(row=0, column=3, sticky="NSEW")

searchlbl = tk.Label(root, text="Search User")
searchlbl.grid(row=2, column=0, sticky="W")

search = tk.Entry(root, width=30)
search.grid(row=2, column=1, sticky="W")


def reset_window():
    dataNo.grid_forget()
    name.grid_forget()
    password.grid_forget()
    userPos.grid_forget()
    pkRes.grid_forget()
    userRes.grid_forget()
    userRes.delete(0, tk.END)
    passRes.grid_forget()
    posList.delete(0, tk.END)
    posList.grid_forget()
    updateBtn.grid_forget()
    deleteBtn.grid_forget()
    
def switch_to_second_window(event):
    root.withdraw()
    reset_window()
    import LoginWindow as login
    login.root.deiconify()


logoutlbl.bind('<Button-1>',switch_to_second_window)

def updateData(row0,row1,row2,row3):
    sql="UPDATE `tblusers` SET `username` = %s , `password` = %s, `userPosition` = %s WHERE `tblusers`.`dataNum` = %s"
    cursor.execute(sql,(row1,row2,row3,row0))
    conn.commit()
    reset_window()

def deleteData(row0):
    sql="DELETE FROM `tblusers` WHERE `tblusers`.`dataNum` = %s"
    cursor.execute(sql,(row0,))
    conn.commit()
    reset_window()


dataNo = tk.Label(root, text="Data No.")
name = tk.Label(root, text="Username")
password = tk.Label(root, text="Password")
userPos = tk.Label(root, text="Position")
pkRes = tk.Label(root, text="")
userRes = tk.Entry(root, width=30)
passRes = tk.Label(root, text="")
posList = tk.Listbox(root, height=0, width=12)
updateBtn= tk.Button(root,text="update", width=10)
deleteBtn= tk.Button(root,text="delete", width=10, fg="red")



def searchResult():
    reset_window()
    sql = "SELECT * FROM tblusers WHERE `username` = %s"
    val=search.get()
    cursor.execute(sql,(val,))
    rows = cursor.fetchone()
    print(rows)
    if rows is not None:
        dataNo.config(text="Data No.", fg="black")
        dataNo.grid(row=3, column=0, sticky="NSEW")
        
        name.grid(row=3, column=1, sticky="NSEW")

        password.grid(row=3, column=2, sticky="NSEW")

        userPos.grid(row=3, column=3, sticky="NSEW")

        pkRes.config(text=rows[3])
        pkRes.grid(row=4, column=0, sticky="NSEW")
        
        userRes.insert(0,rows[0])
        userRes.grid(row=4, column=1, sticky="W")
        
        passRes.config(text=rows[1])
        passRes.grid(row=4, column=2, sticky="NSEW")
        
        orgPos=["n/a","Student","Teacher","Faculty"]
        for position in orgPos:
            posList.insert(tk.END,position)
        posList.grid(row=4, column=3, sticky="W")
        
        for i in range(0,len(orgPos)):
            if(rows[2]==posList.get(i)):
                posList.select_clear(0,tk.END)
                posList.activate(i)
        
        print(posList.get(tk.ACTIVE))
        
        deleteBtn.grid(row=4, column=5, sticky="W")
        updateBtn.grid(row=4, column=4, sticky="W")
        
        updateBtn.config(command=lambda: updateData(rows[3],userRes.get(),rows[1],posList.get(tk.ACTIVE)))
        deleteBtn.config(command=lambda: deleteData(rows[3]))
    else:
        dataNo.config(text="User does not exist", fg="red")
        dataNo.grid(row=3, column=0, sticky="W")
      


searchBtn= tk.Button(root,text="search", width=10, command=searchResult)
searchBtn.grid(row=2, column=2, sticky="W")   

