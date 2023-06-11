from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Text Summarizer")
window.eval('tk::PlaceWindow . center')
window.geometry('1280x720')

frame = Frame(window, width=1000, height=500)
frame.grid(row=0, column=0, padx=115,pady=10)

header = Label(frame, text='Text Summarizer', font=('Arial Bold', 40))
header.grid(row=0,columnspan=3)

input_text = Label(frame, text='Enter your text below:')
input_text.grid(row=1)

input_box = Text(frame, width=150, height = 20)
input_box.grid(row=2)

btn = Button(frame, 
             text='SUMMARIZE',
             width='20')
btn.grid(row=3)

output_text = Label(frame, text='Summary:')
output_text.grid(row=4)

output_box = Text(frame, width=150, height=10)
output_box.grid(row=5)

window.mainloop()