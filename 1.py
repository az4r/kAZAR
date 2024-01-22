import tkinter as tk

root = tk.Tk()
root.title("Rozkład siatek zbrojeniowych na arkuszu")

pixel_size = 20
pixel_offset = pixel_size / 2

def pixel(x, y):
    canvas.create_rectangle(x+pixel_offset, y+pixel_offset, x+pixel_size, y+pixel_size, fill="red")

piksele_w_rzedzie = 10
piksele_w_kolumnie = 20

# Rozmiar płótna
canvas_width = (piksele_w_rzedzie * pixel_size) + pixel_offset * 2
canvas_height = (piksele_w_kolumnie * pixel_size) + pixel_offset * 2
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Odległość między pikselami
odleglosc = pixel_offset

for i in range(piksele_w_rzedzie):
    for j in range(piksele_w_kolumnie):
        pixel(i * odleglosc, j * odleglosc)

root.mainloop()
