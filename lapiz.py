import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import Gtk, GdkPixbuf
import os
import platform
import cpuinfo
import psutil
import socket
import webbrowser

lapiz = Gtk.Window(title = "Lapiz")
lapiz.set_default_size(480, 240)

ui = Gtk.ScrolledWindow()

header = Gtk.HeaderBar()

lapizpc = Gtk.MenuButton()
lapizpc.connect("clicked", lambda lapizpencil:exp.show_all())
lapizpc.set_hexpand(True)

closus = Gtk.Button()
closus.connect("clicked", Gtk.main_quit)

header.pack_start(lapizpc)
header.pack_end(closus)

lapizimg = Gtk.Image.new_from_icon_name("emoji-symbols-symbolic", Gtk.IconSize.BUTTON)
lapizpc.set_image(lapizimg)

closusimg = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.BUTTON)
closus.set_image(closusimg)

header.set_custom_title(lapizpc)
lapiz.set_titlebar(header)

boxus = Gtk.Box()

boxus.set_halign(Gtk.Align.CENTER)
boxus.set_valign(Gtk.Align.CENTER)

def distro():
    with open("/etc/os-release") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("PRETTY_NAME="):
                    return line.strip().split("=")[1].strip('"')

info = Gtk.Label(label = f"OS: {distro()}\nArchitecture: {platform.machine()}\nCPU: {cpuinfo.get_cpu_info()['brand_raw']}\nCPU Cores: {psutil.cpu_count(logical = False)}\nCPU Threads: {psutil.cpu_count(logical = True)}\nRAM: {round(psutil.virtual_memory().total / (1024 ** 3))}gb\nDisk used: {round(psutil.disk_usage('/').total / (1024 ** 3), 2)}gb\nDisk total: {round(psutil.disk_usage('/').used / (1024 ** 3), 2)}\nIP-address: {socket.gethostbyname(socket.gethostname())}")

info.set_justify(Gtk.Justification.CENTER)
info.set_xalign(0.5)

boxus.add(info)

ui.add(boxus)

def distroid():
    with open("/etc/os-release") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("ID="):
                    return line.strip().split("=")[1].strip('"')

def about(widget):
    dialogus = Gtk.AboutDialog()
    
    dialogus.set_program_name("Lapiz")
    dialogus.set_version("10.0")
    dialogus.set_copyright("© 2025 progwi0")
    dialogus.set_comments(f"Simple system information tool on GTK3! (running on {distroid()})")
    
    dialogus.set_website("https://progwi0.github.io/")
    dialogus.set_authors(["progwi0", "chicken banana", "sigma"])
    
    dialogus.set_license_type(Gtk.License.GPL_3_0)
    
    dialogus.run()
    dialogus.destroy()

exp = Gtk.Popover()

menus = Gtk.Box(spacing=1, orientation=Gtk.Orientation.VERTICAL)

newwindows = Gtk.Button(label = "New window")
newwindows.connect("clicked", lambda newwindow:os.system("lapiz"))
menus.pack_start(newwindows, True, True, 0)

mysite = Gtk.Button(label = "My site")
mysite.connect("clicked", lambda mysite:webbrowser.open("https://progwi0.github.io/"))
menus.pack_start(mysite, True, True, 0)

abouts = Gtk.Button(label = "About Lapiz")
abouts.connect("clicked", about)
menus.pack_start(abouts, True, True, 0)

exp.add(menus)

lapizpc.set_popover(exp)

lapiz.add(ui)
lapiz.connect("destroy", Gtk.main_quit)
lapiz.show_all()
