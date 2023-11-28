import tkinter as tk

root = tk.Tk()
root.title("Rozkład wycinków na arkuszu")

wysokosc_arkusza, szerokosc_arkusza = 200, 100
wycinki = []

wycinek_x_1, wycinek_y_1 = 50, 50
wycinki.append(wycinek_x_1)
wycinki.append(wycinek_y_1)

wycinek_x_2, wycinek_y_2 = 200, 200
wycinki.append(wycinek_x_2)
wycinki.append(wycinek_y_2)

def arkusze():
    canvas = tk.Canvas(root, width=szerokosc_arkusza, height=wysokosc_arkusza)
    canvas.pack()
    canvas.create_rectangle(0, 0, 100, 200, fill="green")
    canvas.create_rectangle(0, 0, wycinki[0], wycinki[1], fill="red")

#def rysuj_wycinki():
    #wycinek1 = tk.Canvas(root, width=szerokosc_arkusza, height=wysokosc_arkusza)
    #wycinek1.pack()
    #wycinek1.create_rectangle(0, 0, wycinki[0], wycinki[1], fill="red")

arkusze()
#rysuj_wycinki()
root.mainloop()