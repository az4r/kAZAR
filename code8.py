import tkinter as tk

class KalkulatorOdpadow:
    def __init__(self, szerokosc_arkusza, dlugosc_arkusza):
        self.szerokosc_arkusza = szerokosc_arkusza
        self.dlugosc_arkusza = dlugosc_arkusza
        self.wycinki = []

    def dodaj_wycinek(self, szerokosc, dlugosc):
        self.wycinki.append((szerokosc, dlugosc))

    def oblicz_ilosc_arkuszy(self):
        ilosc_arkuszy = 0
        for wycinek in self.wycinki:
            ilosc_arkuszy += (wycinek[0] * wycinek[1]) / (self.szerokosc_arkusza * self.dlugosc_arkusza)
        return ilosc_arkuszy

    def wizualizuj_rozklad(self):
        root = tk.Tk()
        root.title("Rozkład wycinków na arkuszu")

        canvas = tk.Canvas(root, width=self.szerokosc_arkusza * 2, height=self.dlugosc_arkusza)
        canvas.pack()

        arkusz_1 = (0, 0, self.szerokosc_arkusza, self.dlugosc_arkusza)
        arkusz_2 = None

        for i, wycinek in enumerate(self.wycinki):
            if arkusz_1[1] + wycinek[1] <= self.dlugosc_arkusza:
                # Wycinek mieści się na pierwszym arkuszu
                canvas.create_rectangle(arkusz_1[0], arkusz_1[1], arkusz_1[0] + wycinek[0], arkusz_1[1] + wycinek[1], outline="black", fill="red", tags=f'Wycinek_{i + 1}')
                arkusz_1 = (arkusz_1[0], arkusz_1[1] + wycinek[1], arkusz_1[2], arkusz_1[3])
            elif arkusz_2 is None or arkusz_2[1] + wycinek[1] <= self.dlugosc_arkusza:
                # Wycinek nie mieści się na pierwszym arkuszu, sprawdź drugi arkusz
                if arkusz_2 is None:
                    arkusz_2 = (self.szerokosc_arkusza, 0, self.szerokosc_arkusza * 2, self.dlugosc_arkusza)
                    canvas.create_rectangle(*arkusz_2, outline="black", fill="green", tags='Arkusz2')
                canvas.create_rectangle(arkusz_2[0], arkusz_2[1], arkusz_2[0] + wycinek[0], arkusz_2[1] + wycinek[1], outline="black", fill="red", tags=f'Wycinek_{i + 1}')
                arkusz_2 = (arkusz_2[0], arkusz_2[1] + wycinek[1], arkusz_2[2], arkusz_2[3])
            else:
                # Wycinek nie mieści się na obu arkuszach, dodaj nowy arkusz
                arkusz_1 = (0, arkusz_1[1], self.szerokosc_arkusza, arkusz_1[1] + wycinek[1])
                canvas.create_rectangle(arkusz_1[0], arkusz_1[1], arkusz_1[0] + wycinek[0], arkusz_1[1] + wycinek[1], outline="black", fill="red", tags=f'Wycinek_{i + 1}')

        canvas.create_rectangle(arkusz_1[0], 0, arkusz_1[2], self.dlugosc_arkusza, outline="black", fill="green", tags='Arkusz1')
        if arkusz_2 is not None:
            canvas.create_rectangle(arkusz_2[0], 0, arkusz_2[2], self.dlugosc_arkusza, outline="black", fill="green", tags='Arkusz2')

        # Podnieś czerwone wycinki na wierzch
        for i, wycinek in enumerate(self.wycinki):
            canvas.tag_raise(f'Wycinek_{i + 1}')

        root.mainloop()

# Przykład użycia
kalkulator = KalkulatorOdpadow(szerokosc_arkusza=100, dlugosc_arkusza=200)

kalkulator.dodaj_wycinek(szerokosc=100, dlugosc=100)
kalkulator.dodaj_wycinek(szerokosc=50, dlugosc=50)
kalkulator.dodaj_wycinek(szerokosc=50, dlugosc=50)
kalkulator.dodaj_wycinek(szerokosc=50, dlugosc=50)

ilosc_arkuszy = kalkulator.oblicz_ilosc_arkuszy()
print(f"Ilość potrzebnych arkuszy: {ilosc_arkuszy}")

kalkulator.wizualizuj_rozklad()
