import tkinter as tk
from tkinter import messagebox

def surprise():
    messagebox.showinfo("Surprise!", "สุขสันต์วันเกิด! 🎉 ขอให้มีความสุขมาก ๆ นะ!")

def show_balloons():
    canvas.create_oval(100, 150, 200, 250, fill="red", outline="red")
    canvas.create_oval(200, 100, 300, 200, fill="blue", outline="blue")
    canvas.create_oval(50, 50, 150, 150, fill="yellow", outline="yellow")
    canvas.create_text(200, 300, text="สุขสันต์วันเกิด!", font=("Helvetica", 24), fill="green")

root = tk.Tk()
root.title("Happy Birthday kub")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

btn_surprise = tk.Button(root, text="กดเพื่อเซอร์ไพรส์!", command=lambda: [surprise(), show_balloons()])
btn_surprise.pack(pady=20)

root.mainloop()
