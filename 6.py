import tkinter as tk

root = tk.Tk()
root.title("Rozkład siatek zbrojeniowych na arkuszu")

# Rozmiar pixela
pixel_size = 10
pixel_offset = pixel_size / 2

def pixel(x, y, color):
    canvas.create_rectangle(x, y, x+pixel_size, y+pixel_size, fill=color)
    pixels[y // pixel_size][x // pixel_size] = color  # Zapisywanie informacji o kolorze piksela

# Rozmiar arkusza
piksele_w_rzedzie = 10
piksele_w_kolumnie = 20

# Rozmiar płótna
canvas_width = piksele_w_rzedzie * pixel_size
canvas_height = piksele_w_kolumnie * pixel_size
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Inicjalizacja dwuwymiarowej listy na informacje o kolorach pikseli
pixels = [['green' for _ in range(piksele_w_rzedzie)] for _ in range(piksele_w_kolumnie)]

for i in range(piksele_w_rzedzie):
    for j in range(piksele_w_kolumnie):
        pixel(i * pixel_size, j * pixel_size, 'green')

# Przykładowe wycinki
wycinek1 = ([0, 0], [2, 4])
wycinek2 = [5, 6]

# Sprawdzenie koloru piksela w wycinku i zmiana na czerwony, jeśli jest zielony
for i in range(wycinek1[0][0], wycinek1[1][0] + 1):
    for j in range(wycinek1[0][1], wycinek1[1][1] + 1):
        if pixels[j][i] == 'green':
            pixel(i * pixel_size, j * pixel_size, 'red')

if pixels[wycinek2[1]][wycinek2[0]] == 'green':
    pixel(wycinek2[0] * pixel_size, wycinek2[1] * pixel_size, 'red')

root.mainloop()