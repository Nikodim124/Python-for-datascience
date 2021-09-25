from tkinter import *
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

names = ['Вит. А', 'Вит. B', 'Вит. C', 'Вит. D', 'Вит. E']
products = ['Яблоко', 'Пшено', 'Говядина', 'Творог', 'Конфеты']
colors = ['green', 'yellow', 'red', 'blue', 'white']
vitamins = np.array([[1, 9, 2, 1, 1], [10, 1, 2, 1, 1], [1, 0, 5, 1, 1], [2, 1, 1, 2, 9], [2, 1, 2, 13, 2]])
xs = []
norma = np.array([170, 180, 140, 180, 350]).reshape((5, 1))

def check(a):
    for i in a:
        if i < 0:
            return False
        else:
            return True

def clicked():
    for i in range(len(names)):
        for j in range(len(products)):
            vitamins[j][i] = int(xs[i][j].get())
    sizes = np.ravel(solve(vitamins, norma))
    if check(sizes):
        frameChartsLT = Frame(window)
        frameChartsLT.pack()
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.pie(sizes, labels=names, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()
    else:
        messagebox.showerror('Ошибка', 'Что-то пошло не так')

window = Tk()
window.title('Расчёт продуктов')
window.minsize(width=800, height=600)
app = Frame(window)
app.pack()
colump = 0
rowp = 0
Label(app, text='Продукты').grid(row=rowp, column=columnp)
columnp += 1
for i in names:
    Label(app, text=i).grid(row=rowp, column=columnp)
    columnp += 1
columnp = 0
rowp += 1
for product in products:
    Label(app, text=product).grid(row=rowp, column=columnp)
    columnp += 1
    en_row = []
    for t in range(len(names)):
        e = Entry(app, width=10)
        e.insert(0, vitamins[columnp-1][rowp-1])
        e.grid(column=columnp, row=rowp)
        entry_row.append(e)
        columnp += 1
    xs.append(en_row)
    columnp = 0
    rowp += 1
columnp = 0
rowp += 1
btn = Button(app, text="Рассчитать", command=clicked)
btn.grid(column=columnp, row=rowp)
columnp += 1
errorLabel = Label(app)
errorLabel.grid(row=rowp, column=columnp)

app.bind('<Escape>', lambda x: app.destroy())
app.mainloop()
