import tkinter
import random
import time

window=tkinter.Tk()
window.title('Собери фрукты')
h=800
score = 0


fruit=[]
window.geometry('800x800')
c=tkinter.Canvas(window,width=800,height=h,bg='#43EB75')
c.pack()
def speed_up():
    global speed
    speed=speed+2

but=tkinter.Button(text='увеличить скорость',command=speed_up)
#привязка кнопки к окну
c.create_window((100,100),window=but)

t=c.create_text(120,30,font='Arial 20', fill='red',text='Очки:')
def click_func(event):
    global score
    x_new = event.x
    y_new = event.y
    print(x_new, y_new)
    position = c.coords(id_fr)
    print(position)
    if (position[0]-25<=x_new<=position[0]+25) and (position[1]-25<=y_new<=position[1]+25):
        #print('попал')
        c.delete(id_fr)
        score=score+1
        print(score)
        c.itemconfigure(t,text='Очки:'+str(score))
        

c.bind_all('<Button-1>',click_func)

speed=7
def func():
    for i in range((h-100)//speed):
        c.move(id_fr,0,speed)
        window.update()
        time.sleep(0.02)
    
    

while True:
    img1=tkinter.PhotoImage(file='ananas.png')
    img2=tkinter.PhotoImage(file='banana.png')
    img3=tkinter.PhotoImage(file='apple.png')
    img4=tkinter.PhotoImage(file='orange.png')
    fruit.append(img1)
    fruit.append(img2)
    fruit.append(img3)
    fruit.append(img4)

    r=random.randint(0,3)
    x=random.randint(10,790)
    id_fr=c.create_image(x,0,image=fruit[r])
    func() #движение фрукта

def click_func(event):
    print('sdfg')
    x_new=event.x
    y_new=event.y
    print(x_new,y_new)


c.bind_all('<Button-1>',click_func)

window.mainloop()
