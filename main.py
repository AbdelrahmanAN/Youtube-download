from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk

def Download() :
    file = filedialog.askdirectory(title="Save vedio")
    link = link_entry.get()
    YT=YouTube(link).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(file)
    link_entry_label.configure(text=YT.title)

root = Tk()
root.geometry("600x400")
root.title("Downloading...")

link_entry_label = ttk.Label(root,text="Enter the video link")
link_entry_label.pack(padx = 10, pady = 10)

link_entry = ttk.Entry(root, width=80)
link_entry.pack(padx=10,pady=10)

download_button = ttk.Button(root, text="Download", command=Download)
download_button.pack(padx=10,pady=10)

root.mainloop()