import tkinter as tk
import random
from PIL import Image,ImageTk


window = tk.Tk()
window.title('Bilispider')
window.geometry('960x600')

# load = Image.open('xxxx.jpg')          #此处为背景图片，我就不放了
# render= ImageTk.PhotoImage(load)
# img = tk.Label(window,image=render)
# img.image = render
# img.place(x=0,y=0)


tk.Label(window,text='AV:').place(x=650,y=150)

varav = tk.StringVar()
varav.set('试试手气！')
entry = tk.Entry(window,textvariable=varav)
entry.place(x=700,y=150)                  #选定entry框的位置

from bilibili_support import Spider       

button = tk.Button(window,text='获取视频信息',command = Spider().get_video_info)
button.place(x=700,y=200)                 #选定button参数
button1 = tk.Button(window,text='退出',command = window.destroy)
button1.place(x=800,y=200)
aid= str(random.randint(1,40000000))          #生成随机aid号    

window.mainloop()
