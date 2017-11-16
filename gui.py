"""Docstring."""
import newspaperArticle
import tkinter
import threading

def thread():
    threading._start_new_thread(start1,())

def start1():
    url = getText.get()
    score = newspaperArticle.run(url)
    showResult.set('Result: ' + str(score))

top = tkinter.Tk()
top.title("Newspaper scrapper")
getText = tkinter.StringVar()
input1_label = tkinter.Label(top, text="Article URL:").grid(row = 3,column =1,sticky = 'W',pady=20)
input1_text = tkinter.Entry(top,text = getText, bd =5,width = 50).grid(row =3 ,column =2,sticky = 'W')
submit = tkinter.Button(top,text = 'submit',command = thread).grid(row = 3 ,column = 3,sticky = 'W',padx = 30)

showResult = tkinter.StringVar()
label = tkinter.Label( top, textvariable=showResult ).grid(row = 5)
showResult.set('Result: ')

top.mainloop()
