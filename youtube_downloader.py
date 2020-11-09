# youtube downloader - 02-10-2020
# nithish vasala - python project
# https://youtu.be/I5rN-2TLhq4 - Example URL for testing

# !/usr/lib/python3.8

from pytube import YouTube
from tkinter.ttk import Combobox
from tkinter import ttk, filedialog, Label
from tkinter.messagebox import *
from tkinter import *
from progress.bar import Bar

selectFolder = ''
file_size = 0
# browse folder function
def browsePath():
    global selectFolder
    selectFolder = filedialog.askdirectory(title="choose folder", parent=top,initialdir='/home') # set your initial directory as per your convience
    downloadPath.set(selectFolder)

# download function
def downloadvideo():
    global file_size, yt
    choice = youtubeChoices.get()
    browse1 = browsepath.get()

    url = urlField.get()
    if len(url) > 1:
        urlFieldError.config(text="")
        yt=YouTube(url)
        print(yt.title)
        print(type(yt))
        print(url)

    elif url == '':
        urlFieldError.config(text="Please Enter Youtube Link :", font="verdana 16 bold", fg="red")
        print("Enter Url")
    else:
        urlFieldError.config(text='Error')
        print("Error")

    if len(browse1) > 1:
        print(browse1)
        browsepatherror.config(text=" ")

    elif browse1 == '':
        browsepatherror.config(text="Please enter path to download :",font="verdana 16 bold", fg="red")

    else:
        browsepatherror.config(text="Error :", font="verdana 16 bold", fg="red")


    if choice == downloadChoices[0]:
        selectedVideo = yt.streams.filter(progressive=True).first()
        print(yt.streams.filter(progressive=True).first())
        #selectedVideo.download(selectFolder)

    if choice == downloadChoices[1]:
        selectedVideo = yt.streams.filter(progressive=True).last()
        print(yt.streams.filter(progressive=True,file_extension='mp4').last())
        # selectedVideo.download(selectFolder)

    if choice == downloadChoices[2]:
        selectedVideo = yt.streams.filter(only_audio=True).first()
        print(yt.streams.filter(only_audio=True).first())
        #selectedVideo.download(selectFolder)

    file_size=selectedVideo.filesize
    selectedVideo.download(selectFolder)
    print(selectFolder)
    downloadCompleted()

def downloadCompleted():
    downloadBtn['text'] = "Please wait"
    showinfo("message", 'File has been downloaded..!! and saved in\n' + selectFolder)
    downloadBtn['text'] = "DOWNLOAD"
    downloadBtn['state'] = 'active'
    urlField.delete(0, END)
    browsepatherror.config(text=" ")



# gui coding
top = Tk()
frame1 = Frame(top)
frame1.pack(fill=X)
frame2 = Frame(top)
frame2.pack(fill=X, pady=40)
top.title("Youtube downloader")
top.iconphoto(True, PhotoImage(file="img/youtube.ico"))
top.geometry("600x600")
top.resizable(False, False)

# window label image
file = PhotoImage(file="img/youtube-icon.png")
headingIcon = Label(frame1, image=file)
headingIcon.pack(pady=20)

# url label
l1 = Label(frame1, text="Video Link", font=("verdana", 16))
l1.pack()

# url field
videoLink = StringVar()
urlField = Entry(frame1, font="verdana 20", justify=CENTER, textvariable=videoLink)
urlField.pack(side=TOP, fill=X, padx=10)

urlField.focus()

# url field error :
urlFieldError = Label(frame1, text="", font="verdana 20 bold", fg='red')
urlFieldError.pack()

# Browse label
l2 = Label(frame2, text="Now Select the path", font=("verdana", 16))
l2.grid(columnspan=4, row=0, column=0)

# browse path
downloadPath= StringVar()
browsepath = Entry(frame2, width=25, font="verdana 20",textvariable=downloadPath)
browsepath.grid(padx=10, row=1, sticky=W)

# Browsebutton
browsebutton = Button(frame2, text="Browse", font="verdana 16", width=8, height=1, relief='ridge',activebackground="#00FF00",foreground="black",bg="#32CD32", command=browsePath)
browsebutton.grid(row=1, column=2, columnspan=4)

# Browse path error:
browsepatherror = Label(frame2, text="", font="verdana", fg="red")
browsepatherror.grid()

# dropdown for streams
downloadChoices = ["video/360",
                   "video/720",
                   "Audio/mp4"]

youtubeChoices = Combobox(top, values=downloadChoices, width=27, font="verdana 14",justify=CENTER)
youtubeChoices.pack()
youtubeChoices.current(0)

# download BUTTON
downloadBtn = Button(top, text="DOWNLOAD", font="verdana 20", relief='ridge', justify=CENTER,activebackground="#00FF00",foreground="black", bg="#32CD32",command=downloadvideo)
downloadBtn.pack(pady=30)

top.mainloop()
