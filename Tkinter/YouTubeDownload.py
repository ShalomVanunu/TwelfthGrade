""" this program download the mp4 file from Youtube link"""

from tkinter import *
from pytube import YouTube
import pytube

root = Tk()
root.geometry("400x350")
root.title("Youtube video downloader application")
root.iconbitmap("mp4.ico")

def download():
    try:
        myVar.set("Downloading......")
        root.update()
        YouTube(link.get()).streams.first().download()
        myVar.set("Video downloaded successfully")
#
    #except pytube.exceptions.RegexMatchError as e:
    except:
        myVar.set("Mistake")
        root.update()
        link.set("Enter Valid Link")


Label(root, text="Welcome to Youtube\n downloader Application", font="david 15 bold").pack()

myVar=StringVar()
myVar.set("Enter the link Below")
Entry(root, textvariable=myVar,width=40).pack(pady=10)

link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)

Button(root, text="download Video", command = download).pack(pady=10)

root.mainloop()
