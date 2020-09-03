import Tkinter
from Tkinter import *

from config import *
from text_process import *


iters = 0
idx = 0
pause = True


def pause_system(event=None):
    global pause
    if(not pause):
        pause = True
        print_metrics()

    else:
        pause = False


def go_back(event=None):
    global idx
    global refresh
    global refresh_slow
    global back_words
    idx -= back_words
    idx = max(0, idx)
    refresh = refresh_slow


def go_fast(event=None):
    global refresh
    global refresh_fast
    refresh = refresh_fast


master = Tkinter.Tk()
canvas = Tkinter.Canvas(master, width=w_width, height=w_height)
canvas.pack()
canvas.bind_all("<p>", pause_system)
canvas.bind_all("<k>", go_back)
canvas.bind_all("<l>", go_fast)
canvas.configure(bg=bg_color)
canvas.config(highlightthickness=0)


def clock():
    global iters
    global idx
    global pause
    global font_color

    if(not pause):
        iters += 1
        canvas.delete('all')
        line = ""

        line = book[idx] + " "
        idx += 1
        for I in range(0, len(book)):
            if(len(line) > max_width):
                break
            else:
                line += book[idx] + " "
                idx += 1

        line = line[0:len(line)-1]

        canvas.create_text(w_width/2, w_height/2,
                           font=("Helvetica", font_siz), fill=font_color, text=line)

    master.after(refresh, clock2)


def clock2():
    global pause
    if(not pause):
        canvas.delete('all')

    master.after(1, clock)


def print_metrics():
    page = 0
    print("")
    for I in range(0, len(page_words)):
        page += page_words[I]
        if(page > idx):
            print("Current page: " + str(p_start + I))
            break
    wpm = idx/(0.001*iters*refresh)*60
    minutes = float((len(book)-idx)/wpm)
    seconds = (minutes - int(float((len(book)-idx)/wpm)))*60
    print("wpm = " + str(int(wpm)))
    print("time to read = " + str(int(minutes))+"m "+str(int(seconds))+"s")
    print("")


clock()

book = []

if format_type == Format.PDF_ONE:
    book = pdf_process(book_path)

elif format_type == Format.PDF_TWO:
    book = pdf2_process(book_path)

if format_type == Format.TEXT:
    book = txt_process(book_path)

if format_type == Format.URL:
    book = url_process(book_path)

mainloop()
