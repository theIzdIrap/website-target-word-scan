import tkinter as tk
import requests
import time

root = tk.Tk()
root.geometry("450x200")
root.resizable(False, False)
root.title("Find spesific codes from target website")

def func():
    global u
    url = E1.get()
    klm = B1.get()

    r = requests.get(url, allow_redirects=True)
    with open('1313.txt', 'w+') as f:
        f.write(str(r.content))

    def search_str(file_path, word):
        with open(file_path, 'r') as file:

            content = file.read()

            if word in content:
                u = tk.Label(root, text="website have a target word")
                u.pack()
                u.after(4000,lambda:u.destroy())

            else:
                f = tk.Label(root, text="website doesn't have a target word")
                f.pack()
                f.after(4000, lambda: f.destroy())

    search_str(r'1313.txt', klm)









y = tk.Label(root, text="Website")
y.pack()
E1 = tk.Entry(root, bd =5)
E1.pack()

t = tk.Label(root, text="Word")
t.pack()
B1 = tk.Entry(root, bd =5)
B1.pack()

B = tk.Button(root, text ="Find", command = func)
B.pack()







root.mainloop()
