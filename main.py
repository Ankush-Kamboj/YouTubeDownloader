# importing the modules  
from pytube import YouTube
import tkinter as tk  

root = tk.Tk()
root.geometry("350x300")
root.title("Youtube Downloader")

# input variables
link = tk.StringVar()
save = tk.StringVar()

def downloadVideo():
    url = link.get()
    
    # where to save  
    SAVE_PATH = "E:/YouTube/" #to_do 
    
    try:  
        # object creation  
        yt = YouTube(url)  
    except:  
        print("Connection Error") #to handle exception  
      
    
    stream = yt.streams.first()

    stream.download(SAVE_PATH)


w = tk.Label(root, text="Youtube Downloader", font=("Serif", 24))
w.place(x=20, y=20)

linkinput = tk.Label(root, text="Enter the url of video", font=("Serif",14))
linkinput.place(x=80, y=80)

linkEntry = tk.Entry(root, textvariable=link, width=30)
linkEntry.place(x=80, y=120)

saveinput = tk.Label(root, text="Enter save location", font=("Serif",14))
saveinput.place(x=80, y=150)

saveEntry = tk.Entry(root, textvariable=save, width=30)
saveEntry.place(x=80, y=180)

btn = tk.Button(root, text="Download", width=10, command=downloadVideo)
btn.place(x=130, y=220)

root.mainloop()