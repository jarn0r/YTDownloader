import tkinter
import customtkinter
from customtkinter import filedialog
from pytube import YouTube

def startDownloadMP4():
    try:
        ytLink = link.get()
        my_path = save_path.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download(output_path=my_path)
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Downloaded failed, Link invalid",text_color = "red")

def startDownloadMP3():
    try:
        ytLink = link.get()
        my_path = save_path.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download(output_path=my_path)
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Downloaded failed, Link invalid",text_color = "red")

def browse_path():
    path = filedialog.askdirectory()
    path_entry.delete(0, customtkinter.END)  # Clear any previous entry
    path_entry.insert(0, path)
#System Setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI Elements
title = customtkinter.CTkLabel(app, text="Dein YT Link")
title.pack(padx=10,pady=10)

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download MP4", command=startDownloadMP4)
download.pack(padx=10,pady=5)

download2 = customtkinter.CTkButton(app, text="Download MP3", command=startDownloadMP3)
download2.pack(padx=10,pady=5)

finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack(padx=10,pady=10)

save_path = customtkinter.StringVar()
path_entry = customtkinter.CTkEntry(app, width=800, height=42, font=('Arial', 20), textvariable=save_path)
path_entry.pack(padx=10,pady=5)

browse_button = customtkinter.CTkButton(app, text="Browse", width=200, height=42, font=('Arial', 20), command=browse_path)
browse_button.pack(padx=10,pady=5)
#Run
app.mainloop()