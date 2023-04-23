import tkinter
import random
window = tkinter.Tk() #samoe verhnee okno
window.title("Самостоятельная работа 3.1")
window.geometry('1200 x 650 + 375 + 200')
c = tkinter.Canvas(window, width = 1100, height = 650, bg = "#000080")
c.create_text(100, 25, font = "Arial 14 bold italic", text = "2M002")
c.pack()
c.create_oval(200, 550, 1300, 900, fill = "#FFFFFF")

c.create_rectangle(500, 500, 600, 600, fill = "#56280B")

c.create_polygon([850, 500], [250, 500], [550, 300], fill = "#228B22", outline = "#002800")
c.create_polygon([750, 400], [350, 400], [550, 250], fill = "#228B22", outline = "#002800")
c.create_polygon([650, 300], [450, 300], [550, 150], fill = "#228B22", outline = "#002800")

c.create_polygon([500, 200], [570, 150], [550, 100], fill = "#D1E231", outline = "#2F3201")
c.create_polygon([600, 200], [530, 150], [550, 100], fill = "#D1E231", outline = "#2F3201")
c.create_polygon([610, 130], [550, 165], [490, 130], fill = "#D1E231", outline = "#2F3201")
