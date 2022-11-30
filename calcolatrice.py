from tkinter import *

window_calcolatrice=Tk()
window_calcolatrice.title('CALCOLATRICE')
window_calcolatrice.geometry('400x600')

display = Entry(window_calcolatrice)
display.grid(row=0, column=0, columnspan=3)

for rw in range(4):
    for cl in range(3):
        f = Frame(window_calcolatrice)
        f.grid(row=rw+1, column=cl)
        tasti_calcolatrice=Button(f).pack()



window_calcolatrice.mainloop()