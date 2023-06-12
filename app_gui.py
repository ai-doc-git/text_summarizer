from tkinter import *
from tkinter.ttk import *

from model import text_summarization

# function
def summarize():
    input_val = input_box.get("1.0",END)
    output_val = text_summarization(input_val)
    output_box.delete(1.0,"end")
    output_box.insert(1.0, output_val)

# window
window = Tk()
window.title("Text Summarizer")
window.eval('tk::PlaceWindow . center')
window.geometry('1280x720')


# frame
frame = Frame(window, width=1000, height=500)
frame.grid(row=0, column=0, padx=115,pady=10)


# header
header = Label(frame, text='Text Summarizer', font=('Arial Bold', 40))
header.grid(row=0,columnspan=3)


# input text
input_text = Label(frame, text='Enter your text below:')
input_text.grid(row=1)


#input box
input_box = Text(frame, width=150, height = 20)
input_box.grid(row=2)


# button
btn = Button(frame, text='SUMMARIZE', width='20', command=summarize)
btn.grid(row=3)


# output text
output_text = Label(frame, text='Summary:')
output_text.grid(row=4)


# output box
output_box = Text(frame, width=150, height=10)
output_box.grid(row=5)

window.mainloop()