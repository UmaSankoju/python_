import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sankojuuma@25",
    database="login_system"
)

mycursor = mydb.cursor()

root = tk.Tk()
root.title("Login Form")
root.geometry('500x500')

attempts = 0

def show_msg():
    global attempts
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Please enter username & password")
        return

    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    values = (username, password)

    mycursor.execute(sql, values)
    result = mycursor.fetchone()

    if result:   
        messagebox.showinfo("Success", "Login Successful!")
    else:
        attempts += 1
        if attempts < 3:
            messagebox.showerror("Failed", f"Invalid credentials. Attempts left: {3 - attempts}")
        else:
            messagebox.showerror("Blocked", "You are out of attempts! Try again later.")

tk.Label(root, text="Hello Tkinter!", font=('Arial', 20)).grid(row=1, column=0, columnspan=2, pady=20)

tk.Label(root, text="User Name :", font=("Arial", 15)).grid(row=2, column=0, padx=10, pady=15)
username_entry = tk.Entry(root)
username_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Password :", font=("Arial", 15)).grid(row=3, column=0, padx=10, pady=15)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text='Login', command=show_msg).grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
