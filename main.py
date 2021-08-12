import pyautogui
from tkinter import *

cmyk_scale = 100


def from_rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def show_mouse_pos(last=None):
    xy = window.winfo_pointerxy()
    if xy != last:
        xy = str(xy).replace(')', '').replace('(', '').replace(',', '').split()
        titleXY['text'] = 'X:' + xy[0] + ', Y:' + xy[1]

        pixelColor = pyautogui.screenshot().getpixel((int(xy[0]), int(xy[1])))
        textColor = 'RGB\nR:' + str(pixelColor[0]).rjust(3)
        textColor += '\nG:' + str(pixelColor[1]).rjust(3)
        textColor += '\nB:' + str(pixelColor[2]).rjust(3)

        titleRGB['text'] = textColor

        frame['bg'] = from_rgb(pixelColor[0], pixelColor[1], pixelColor[2])

        last = xy
    window.after(100, show_mouse_pos, xy)


window = Tk()
window['bg'] = '#ffffff'
window.title('WTC')
window.geometry('250x130')
window.iconbitmap('WTCiCO.ico')
window.attributes("-topmost", True)
window.resizable(width=False, height=False)

frame = Frame(window)
frame.place(relx=0.05, rely=0.1, width=100, height=100)

titleXY = Label(window, text='blabla', font='Fixedsys 14')
titleXY.place(relx=0.5, rely=0.1)

titleRGB = Label(window, text='blabla', font='Fixedsys 14', justify='left')
titleRGB.place(relx=0.5, rely=0.3)

show_mouse_pos()

window.mainloop()
