import tkinter as tk
import random
from PIL import Image,ImageTk


window = tk.Tk()
window.title('Bilispider')
window.geometry('960x600')

load = Image.open('IMG_3375.jpg') 
render= ImageTk.PhotoImage(load)
img = tk.Label(window,image=render)
img.image = render
img.place(x=0,y=0)


tk.Label(window,text='AV:').place(x=650,y=150)

varav = tk.StringVar()
varav.set('试试手气！')
entry = tk.Entry(window,textvariable=varav)
entry.place(x=700,y=150)

from bilibili_support import Spider

button = tk.Button(window,text='获取视频信息',command = Spider().get_video_info)
button.place(x=700,y=200)
button1 = tk.Button(window,text='退出',command = window.destroy)
button1.place(x=800,y=200)
aid= str(random.randint(1,20000000))

window.mainloop()
