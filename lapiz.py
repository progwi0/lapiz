from tkinter import *
from tkinter import messagebox as dialogus
import os
import webbrowser
import platform
import cpuinfo
import psutil
import socket

app = Tk()
app.title("Lapiz")

def info():
    dialogus.showinfo("✏️", "Lapiz 1.0\nCreated in 2025 by progwi0.")

lapiz = Button(app, text = "✏️", command = lambda:menu.post(app.winfo_pointerx(), app.winfo_pointery()))
lapiz.pack(fill = "x")

menu = Menu(app, tearoff = 0)

menu.add_separator()
menu.add_command(label="Reinstall (Only for pix version)", command = lambda:os.system("pix reinstall lapiz"))
menu.add_separator()
menu.add_command(label="My site", command = lambda:webbrowser.open("https://progwi0.github.io/"))
menu.add_command(label="About", command = info)
menu.add_separator()

os = Label(app, text = f"OS: {platform.system()} {platform.release()}")
os.pack(pady="10", padx="30")

arch = Label(app, text = f"Architecture: {platform.machine()}")
arch.pack(pady="10", padx="30")

cpu = Label(app, text = f"CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
cpu.pack(pady="10", padx="30")

cores = Label(app, text = f"Cores: {psutil.cpu_count(logical = False)}")
cores.pack(pady="10", padx="30")

threads = Label(app, text = f"Threads: {psutil.cpu_count(logical = True)}")
threads.pack(pady="10", padx="30")

ram = Label(app, text = f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3))}gb")
ram.pack(pady="10", padx="30")

disktotal = Label(app, text = f"Disk Total: {round(psutil.disk_usage('/').total / (1024 ** 3), 2)}gb")
disktotal.pack(pady="10", padx="30")

diskused = Label(app, text = f"Disk Used: {round(psutil.disk_usage('/').used / (1024 ** 3), 2)}gb")
diskused.pack(pady="10", padx="30")

ip = Label(app, text = f"IP-adress: {socket.gethostbyname(socket.gethostname())}")
ip.pack(pady="10", padx="30")

app.mainloop()
