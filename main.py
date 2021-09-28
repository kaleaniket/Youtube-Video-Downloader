from tkinter import *
from pytube import YouTube

window = Tk()
window.config(bg="gray")
window.geometry("500x300")
window.title("Aniket's Youtube Video Downloader")

Label(window, text="Youtube Video Downloader", font=("arial", 20, "bold"), bg="gray", pady=10).pack()

link = StringVar()
Label(window, text='Paste Link Here:', font=("arial", 15, "bold"), bg="gray").place(x=160, y=60)
link_enter = Entry(window, width=70, textvariable=link).place(x=32, y=90)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.filter(resolution="1440p").first()
    path = "C:/Users/Aniket/Desktop/YoutubeDownloaded"
    video.download(path)

    Label(window, text="DOWNLOADED", font=("arial", 15, "italic")).place(x=180, y=210)


Button(window, text="DOWNLOAD", font=("arial", 15, "bold"), padx=2, command=downloader).place(x=150, y=150)

window.mainloop()