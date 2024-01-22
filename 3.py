import tkinter as tk

root = tk.Tk()
root.title("Rozkład siatek zbrojeniowych na arkuszu")

# Rozmiar pixela
pixel_size = 20
pixel_offset = pixel_size / 2

def pixel(x, y):
    canvas.create_rectangle(x, y, x+pixel_size, y+pixel_size, fill="green")

# Rozmiar arkusza
piksele_w_rzedzie = 10
piksele_w_kolumnie = 20

# Rozmiar płótna
canvas_width = piksele_w_rzedzie * pixel_size
canvas_height = piksele_w_kolumnie * pixel_size
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

for i in range(piksele_w_rzedzie):
    for j in range(piksele_w_kolumnie):
        pixel(i * pixel_size, j * pixel_size)

root.mainloop()