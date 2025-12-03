import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def show_pie():
    try:
        s1 = sub1.get() or "Subject 1"
        s2 = sub2.get() or "Subject 2"
        s3 = sub3.get() or "Subject 3"

        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())

        subjects = [s1, s2, s3]
        marks = [m1, m2, m3]

        plt.pie(marks, labels=subjects, autopct="%1.1f%%")
        plt.title("Marks Comparison")
        plt.show()

        total = sum(marks)
        average = total / 3
        percent = (total / 300) * 100
        stats_lbl.config(text=f"Total: {total} | Avg: {average:.2f} | %: {percent:.2f}%")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric marks!")

def reset_fields():
    for e in [entry1, entry2, entry3, sub1, sub2, sub3]:
        e.delete(0, tk.END)
    stats_lbl.config(text="")


root = tk.Tk()
root.title("Marks Pie Chart")

root.geometry("550x550") 
root.resizable(False, False)


frame = tk.Frame(root, width=500, height=500, bd=3, relief="ridge", padx=10, pady=10, bg="#f0f0f0")
frame.pack(padx=20, pady=20)
frame.pack_propagate(False)  


tk.Label(frame, text="Subject 1:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
sub1 = tk.Entry(frame, width=12)
sub1.grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame, text="Marks 1:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
entry1 = tk.Entry(frame, width=8)
entry1.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame, text="Subject 2:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
sub2 = tk.Entry(frame, width=12)
sub2.grid(row=1, column=1, padx=5, pady=5)
tk.Label(frame, text="Marks 2:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
entry2 = tk.Entry(frame, width=8)
entry2.grid(row=1, column=3, padx=5, pady=5)


tk.Label(frame, text="Subject 3:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
sub3 = tk.Entry(frame, width=12)
sub3.grid(row=2, column=1, padx=5, pady=5)
tk.Label(frame, text="Marks 3:").grid(row=2, column=2, sticky="w", padx=5, pady=5)
entry3 = tk.Entry(frame, width=8)
entry3.grid(row=2, column=3, padx=5, pady=5)


tk.Button(frame, text="Show Pie Chart", command=show_pie, bg="#4CAF50", fg="white", width=20).grid(row=3, column=0, columnspan=2, pady=15)
tk.Button(frame, text="Reset", command=reset_fields, bg="#f44336", fg="white", width=20).grid(row=3, column=2, columnspan=2, pady=15)


stats_lbl = tk.Label(frame, text="", font=("Arial", 10, "bold"), bg="#f0f0f0")
stats_lbl.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
