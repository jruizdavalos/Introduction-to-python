import tkinter as tk
from compressModule import comprees,decompress
from tkinter import filedialog


def open_file():
  filename=filedialog.askopenfilename(initialdir='/',title="Select a tile to compress")
  return filename
def compression(i,o):
  comprees(i,o)


window= tk.Tk()

window.title("Compression engine ")
window.geometry("800x600")

input_entry= tk.Entry(window)
output_entry=tk.Entry(window)

#compress_button= tk.Button(window,text="Compress",command=lambda:compression(input_entry.get(),output_entry.get()))
compress_button= tk.Button(window,text="Compress",command=lambda:compression(open_file(),'comoutput1.txt'))
input_label= tk.Label(window, text="File to be compressed")
output_label= tk.Label(window, text="Name of the compressed file")

input_label.grid(row=0,column=0)
input_entry.grid(row=0,column=1)

output_label.grid(row=1,column=0)
output_entry.grid(row=1,column=1)

compress_button.grid(row=2,column=1)
window.mainloop()

