
from cgitb import text
from email import message
import sys,os
from tkinter import simpledialog
from tkinter.font import BOLD
from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox



window = Tk()
window.title('Youtube Download Mp3')
window.geometry('500x400')


def run():
    varContent = Youtube_Link.get() # get what's written in the inputentry entry widget
    varpath = File_path_name.get()
    PATH = varpath
    URL = varContent
    yt = YouTube(URL)
    try:
        status_text.set("Downloading.....")
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(f"{PATH}")
        
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"    
        os.rename(out_file, new_file)
        status_text.set("Successfully Download")
        
        
        
    except: 
        status_text.set('Something Went Wrong! Please try again')
    
          
        
        
#def create_button(txt):
#    bt_1 = tk.Button(window, text=txt, bg='red', fg='white', font=('Arial', 12))
#    bt_1['width'] = 50
 #   bt_1['height'] = 4
 #   bt_1['activebackground'] = 'red'
 #   bt_1.grid(column=0, row=0)
#create_button('button')

# window.geometry("600x600")
ProgName = ttk.Label(window, text='Youtube download Mp3', font=('Arial', 24, 'bold'))
ProgName.grid(row=2, column=3, pady=20, padx=50)

Youtube_Link = StringVar()
Youtube_Link = ttk.Entry (window, width=50,  textvariable=Youtube_Link )
Youtube_Link.grid(row=4, column=3, pady=10, padx=50)

File_path_name = StringVar()
File_path_name = ttk.Entry (window, width=50,  textvariable=File_path_name )
File_path_name.grid(row=7, column=3, pady=10, padx=50)
        
File_path =ttk.Label(window, text="Download File Path")
File_path.grid(row=6, column=3, pady=10, padx=50)

Youtube_d = ttk.Label(window, text="Please enter youtube video url: ", font=('Aria', 12, 'bold'))
Youtube_d.grid(row=3, column=3, pady=10, padx=50)

submit = ttk.Button(window, text="Download", command=run).grid(row=8, column=3, pady=10, padx=50)
 
status_text = StringVar()
status_result = ttk.Entry(window, textvariable=status_text)

outputtext = ttk.Label(window, textvariable=status_text, font=('Aria', 12, 'bold'))
outputtext.grid(row=9, column=3, pady=10, padx=50)

window.mainloop()
