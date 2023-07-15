from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
import numpy as np
import pandas as pd
import statistics


#Математическая часть
def calculate():
    a1 = float(b1_tf.get())
    a2 = float(b2_tf.get())
    a3 = float(b3_tf.get())
    a4 = float(b4_tf.get())
    a5 = float(b5_tf.get())
    a6 = float(b6_tf.get())
    a7 = float(b7_tf.get())
    a8 = float(b8_tf.get())
    a9 = float(b9_tf.get())
    a10 = float(b10_tf.get())
    a11 = float(b11_tf.get())
    a12 = float(b12_tf.get())
    a13 = float(b13_tf.get())
    a14 = float(b14_tf.get())
    a15 = float(b15_tf.get())
    a16 = float(b16_tf.get())
    a17 = float(b17_tf.get())
    a18 = float(b18_tf.get())
    a19 = float(b19_tf.get())
    a20 = float(b20_tf.get())

    avg=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20]
    average = statistics.mean(avg)
    print("Среднее значение:", average)
    print (len(avg))
    std_deviation = statistics.stdev(avg)/(len(avg) ** 0.5)
    std_deviation =round(std_deviation, 6)
    print("Стандартное отклонение:", std_deviation)
    messagebox.showinfo('Выходные данные', f'Ср.значение: {average} \n'  f'СКО: {std_deviation} ')

def open_file ():
    wanted_files = (

            ("TEXT files", "*.txt"),
        )

    file_name = fd.askopenfile (filetypes=wanted_files)
    if filename:
        with open (file_name,"r") as file:
            avg.insert = (END,file.read())
            average.insert = (END,file.read())
            std_deviation.insert = (END,file.read())
            file.close()

def save_file():
    name = fd.asksaveasfilename(filetypes=(("TEXT files", "*.txt"), ("Py files", "*.py")))
    if name:
        avg.insert(END, f"Сохранить файл по пути {name}\n")
        average.insert = (END,f"Сохранить файл по пути {name}\n" )
        std_deviation.insert = (END, f"Сохранить файл по пути {name}\n")
        file.close()

#Оформление программмы
window = Tk()
window.title('Подсчет погрешностей')
window.geometry('400x600')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

combo = Combobox(frame)
combo['values'] = (1, 2, 3, 4, 5, "СТО АЦ 3.007-2014")
combo.current(5) # установите вариант по умолчанию
combo.grid(column=2, row=0)

combo = Combobox(frame)
combo['values'] = ("S", "C","H\u20820","N","SO\u2083","H\u2082SO\u2084")
combo.current(1) # установите вариант по умолчанию
combo.grid(column=3, row=0)

height0_lb = Label(
    frame,
    text=" № Опыта "
)
height0_lb.grid(row=2, column=1)

height1_lb = Label(
    frame,
    text="1 "
)
height1_lb.grid(row=3, column=1)

height2_lb = Label(
    frame,
    text="2 ",
)
height2_lb.grid(row=4, column=1)

height3_lb = Label(
    frame,
    text="3 "
)
height3_lb.grid(row=5, column=1)

height4_lb = Label(
    frame,
    text="4 ",
)
height4_lb.grid(row=6, column=1)

height5_lb = Label(
    frame,
    text="5 "
)
height5_lb.grid(row=7, column=1)

height6_lb = Label(
    frame,
    text="6 ",
)
height6_lb.grid(row=8, column=1)

height7_lb = Label(
    frame,
    text="7 "
)
height7_lb.grid(row=9, column=1)

height8_lb = Label(
    frame,
    text="8 ",
)
height8_lb.grid(row=10, column=1)

height9_lb = Label(
    frame,
    text="9 "
)
height9_lb.grid(row=11, column=1)

height10_lb = Label(
    frame,
    text="10 ",
)
height10_lb.grid(row=12, column=1)

b1_tf = Entry(
    frame,
)
b1_tf.grid(row=3, column=2, pady=5)

b2_tf = Entry(
    frame,
)
b2_tf.grid(row=3, column=3, pady=5)

b3_tf = Entry(
    frame,
)
b3_tf.grid(row=4, column=2, pady=5)

b4_tf = Entry(
    frame,
)
b4_tf.grid(row=4, column=3, pady=5)

b5_tf = Entry(
    frame,
)
b5_tf.grid(row=5, column=2, pady=5)

b6_tf = Entry(
    frame,
)
b6_tf.grid(row=5, column=3, pady=5)

b7_tf = Entry(
    frame,
)
b7_tf.grid(row=6, column=2, pady=5)

b8_tf = Entry(
    frame,
)
b8_tf.grid(row=6, column=3, pady=5)

b9_tf = Entry(
    frame,
)
b9_tf.grid(row=7, column=2, pady=5)

b10_tf = Entry(
    frame,
)
b10_tf.grid(row=7, column=3, pady=5)

b11_tf = Entry(
    frame,
)
b11_tf.grid(row=8, column=2, pady=5)

b12_tf = Entry(
    frame,
)
b12_tf.grid(row=8, column=3, pady=5)

b13_tf = Entry(
    frame,
)
b13_tf.grid(row=9, column=2, pady=5)

b14_tf = Entry(
    frame,
)
b14_tf.grid(row=9, column=3, pady=5)

b15_tf = Entry(
    frame,
)
b15_tf.grid(row=10, column=2, pady=5)

b16_tf = Entry(
    frame,
)
b16_tf.grid(row=10, column=3, pady=5)

b17_tf = Entry(
    frame,
)
b17_tf.grid(row=11, column=2, pady=5)

b18_tf = Entry(
    frame,
)
b18_tf.grid(row=11, column=3, pady=5)

b19_tf = Entry(
    frame,
)
b19_tf.grid(row=12, column=2, pady=5)

b20_tf = Entry(
    frame,
)
b20_tf.grid(row=12, column=3, pady=5)

cal_btn = Button(
    frame,
    text='Рассчитать ',
    command=calculate
)
cal_btn.grid(row=13, column=2, pady=10)

cal_btn = Button(
    frame,
    text='Открыть файл',
    command=open_file
)
cal_btn.grid(row=16, column=2,  pady=10)

cal_btn = Button(
    frame,
    text='Сохранить файл',
    command=save_file
)
cal_btn.grid(row=16, column=3,  pady=10)

window.mainloop()