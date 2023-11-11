import tkinter as tk
from tkinter import ttk
import random

class AdvancedAlgorithm:
    def __init__(self, green_area_width, green_area_height):
        self.green_area_width = green_area_width
        self.green_area_height = green_area_height
        self.red_areas = []

    def generate_more_placements(self, num_placements):
        placements = []
        for _ in range(num_placements):
            x_position = random.randint(0, self.green_area_width)
            y_position = random.randint(0, self.green_area_height)
            placements.append((x_position, y_position))
        return placements

    def is_collision(self, new_area, existing_areas):
        for area in existing_areas:
            if (
                new_area[0] < area[2]
                and new_area[2] > area[0]
                and new_area[1] < area[3]
                and new_area[3] > area[1]
            ):
                return True
        return False

    def optimize_placement(self, num_red_areas, red_area_data):
        placements = []
        for data in red_area_data:
            poz, b, h, ilosc = data
            b, h, ilosc = int(b), int(h), int(ilosc)
            for _ in range(ilosc):
                new_area = (0, 0, b, h)
                while self.is_collision(new_area, placements):
                    x_position = random.randint(0, self.green_area_width - b)
                    y_position = random.randint(0, self.green_area_height - h)
                    new_area = (x_position, y_position, x_position + b, y_position + h)
                placements.append(new_area)
        return placements

class Ui_MainWindow:
    def __init__(self, root):
        self.root = root
        root.title("kAZAR - kalkulator siatek zbrojeniowych")
        root.geometry("900x400")

        self.centralwidget = tk.Frame(root)
        self.centralwidget.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("TButton", padding=(10, 3, 10, 3), borderwidth=5, relief="raised")

        self.szerokosc_var = tk.StringVar()
        self.wysokosc_var = tk.StringVar()
        self.szerokosc_var.set("100")
        self.wysokosc_var.set("120")

        self.szerokosc_label = tk.Label(self.centralwidget, text="Szerokość arkusza:")
        self.szerokosc_label.place(x=330, y=10, width=131, height=22)
        self.szerokosc_entry = tk.Entry(self.centralwidget, textvariable=self.szerokosc_var)
        self.szerokosc_entry.place(x=330, y=40, width=131, height=22)

        self.wysokosc_label = tk.Label(self.centralwidget, text="Wysokość arkusza:")
        self.wysokosc_label.place(x=470, y=10, width=131, height=22)
        self.wysokosc_entry = tk.Entry(self.centralwidget, textvariable=self.wysokosc_var)
        self.wysokosc_entry.place(x=470, y=40, width=131, height=22)

        self.lineEdit = tk.Entry(self.centralwidget, width=10)
        self.lineEdit.place(x=25, y=210)

        self.lineEdit_2 = tk.Entry(self.centralwidget, width=10)
        self.lineEdit_2.place(x=95, y=210)

        self.lineEdit_3 = tk.Entry(self.centralwidget, width=10)
        self.lineEdit_3.place(x=165, y=210)

        self.lineEdit_4 = tk.Entry(self.centralwidget, width=10)
        self.lineEdit_4.place(x=235, y=210)

        self.pushButton1 = ttk.Button(self.centralwidget, text="Dodaj", width=70, command=self.dodaj_wiersz)
        self.pushButton1.place(x=20, y=235, width=80, height=28)

        self.pushButton1_2 = ttk.Button(self.centralwidget, text="Zmień", width=70, command=self.zmien_wiersz)
        self.pushButton1_2.place(x=120, y=235, width=80, height=28)

        self.pushButton1_3 = ttk.Button(self.centralwidget, text="Usuń", width=70, command=self.usun_wiersz)
        self.pushButton1_3.place(x=223, y=235, width=80, height=28)

        self.pushButton_generate = ttk.Button(self.centralwidget, text="Generuj", width=70, command=self.generuj)
        self.pushButton_generate.place(x=20, y=275, width=283, height=28)

        self.tableWidget = ttk.Treeview(self.centralwidget, columns=(1, 2, 3, 4), show="headings")
        self.tableWidget.place(x=21, y=10, width=282, height=192)
        self.tableWidget.heading(1, text="Poz.")
        self.tableWidget.heading(2, text="b")
        self.tableWidget.heading(3, text="h")
        self.tableWidget.heading(4, text="Ilość")

        self.tableWidget.column(1, width=70)
        self.tableWidget.column(2, width=70)
        self.tableWidget.column(3, width=70)
        self.tableWidget.column(4, width=70)

        self.groupBox = tk.LabelFrame(self.centralwidget, text="Wynik")
        self.groupBox.place(x=330, y=80, width=551, height=261)

        self.frame_width = int(self.szerokosc_var.get())
        self.frame_height = int(self.wysokosc_var.get())

        self.canvas = tk.Canvas(self.groupBox, bg="green", width=self.frame_width, height=self.frame_height)
        self.canvas.place(x=10, y=50)

        self.advanced_algorithm = AdvancedAlgorithm(self.frame_width, self.frame_height)

        self.sample_data = [
            ("1", "40", "50", "1"),
        ]

        for data in self.sample_data:
            self.tableWidget.insert("", "end", values=data)

        self.tableWidget.bind('<ButtonRelease-1>', self.zaznaczenie_wiersza)

    def dodaj_wiersz(self):
        poz = self.lineEdit.get()
        b = self.lineEdit_2.get()
        h = self.lineEdit_3.get()
        ilosc = self.lineEdit_4.get()

        if poz and b and h and ilosc:
            self.tableWidget.insert("", "end", values=(poz, b, h, ilosc))
        else:
            print("Wprowadź wszystkie dane.")

    def zmien_wiersz(self):
        selected_item = self.tableWidget.selection()
        if not selected_item:
            print("Nie wybrano wiersza do zmiany.")
            return

        selected_item = selected_item[0]
        values = self.tableWidget.item(selected_item, 'values')

        poz = self.lineEdit.get()
        b = self.lineEdit_2.get()
        h = self.lineEdit_3.get()
        ilosc = self.lineEdit_4.get()

        if poz and b and h and ilosc:
            self.tableWidget.item(selected_item, values=(poz, b, h, ilosc))
        else:
            print("Wprowadź wszystkie dane.")

    def usun_wiersz(self):
        selected_item = self.tableWidget.selection()
        if not selected_item:
            print("Nie wybrano wiersza do usunięcia.")
            return

        for item in selected_item:
            self.tableWidget.delete(item)

    def zaznaczenie_wiersza(self, event):
        selected_item = self.tableWidget.selection()
        if not selected_item:
            return
        selected_item = selected_item[0]
        values = self.tableWidget.item(selected_item, 'values')

        if values:
            self.lineEdit.delete(0, 'end')
            self.lineEdit.insert(0, values[0])
            self.lineEdit_2.delete(0, 'end')
            self.lineEdit_2.insert(0, values[1])
            self.lineEdit_3.delete(0, 'end')
            self.lineEdit_3.insert(0, values[2])
            self.lineEdit_4.delete(0, 'end')
            self.lineEdit_4.insert(0, values[3])

    def update_red_areas(self):
        for area in self.advanced_algorithm.red_areas:
            self.canvas.delete(area)

        num_red_areas = sum([int(data[3]) for data in self.advanced_algorithm.red_area_data])
        placements = self.advanced_algorithm.optimize_placement(num_red_areas, self.advanced_algorithm.red_area_data)

        for data in self.advanced_algorithm.red_area_data:
            poz, b, h, ilosc = data
            b, h, ilosc = int(b), int(h), int(ilosc)

            for _ in range(ilosc):
                if placements:
                    placement = placements.pop(0)
                    red_area = self.canvas.create_rectangle(
                        placement[0], placement[1], placement[2], placement[3], fill="red", outline="black"
                    )
                    self.advanced_algorithm.red_areas.append(red_area)

        for red_area in self.advanced_algorithm.red_areas:
            self.canvas.tag_raise(red_area)

    def generuj(self):
        for area in self.advanced_algorithm.red_areas:
            self.canvas.delete(area)
        self.advanced_algorithm.red_areas.clear()

        self.advanced_algorithm.red_area_data = []
        for child in self.tableWidget.get_children():
            values = self.tableWidget.item(child, 'values')
            self.advanced_algorithm.red_area_data.append(values)

        self.update_red_areas()

        self.canvas.delete("green_area")

        self.frame_width = int(self.szerokosc_var.get())
        self.frame_height = int(self.wysokosc_var.get())

        self.canvas.config(width=self.frame_width, height=self.frame_height)

        green_area = self.canvas.create_rectangle(
            0, 0, self.frame_width, self.frame_height, fill="green", outline="black", tags="green_area"
        )
        self.canvas.tag_lower(green_area)

        # Zastosuj zaawansowany algorytm
        self.advanced_algorithm.green_area_width = int(self.szerokosc_var.get())
        self.advanced_algorithm.green_area_height = int(self.wysokosc_var.get())
        num_red_areas = len(self.advanced_algorithm.red_areas)

        # Spróbuj wygenerować dodatkowe pozycje, jeśli lista jest pusta
        if not self.advanced_algorithm.red_areas:
            placements = self.advanced_algorithm.generate_more_placements(num_red_areas)
            self.advanced_algorithm.red_areas.extend(placements)

        placements = self.advanced_algorithm.optimize_placement(num_red_areas, self.advanced_algorithm.red_area_data)

        # Aktualizuj czerwone obszary
        for i, red_area in enumerate(self.advanced_algorithm.red_areas):
            placement = placements[i]
            self.canvas.coords(red_area, placement[0], placement[1], placement[2], placement[3])

if __name__ == "__main__":
    root = tk.Tk()
    app = Ui_MainWindow(root)
    root.mainloop()
