#
import tkinter as tk

def say_hello():
    label.config(text="こんにちは！")

root = tk.Tk()
root.title("Hello App")

label = tk.Label(root, text="ようこそ")
label.pack()

button = tk.Button(root, text="挨拶する", command=say_hello)
button.pack()

root.mainloop()
