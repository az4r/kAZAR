import tkinter as tk
from tkinter import ttk

class Ui_MainWindow:
    def __init__(self, root):
        self.root = root
        root.title("MainWindow")
        root.geometry("900x400")

        self.centralwidget = tk.Frame(root)
        self.centralwidget.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("TButton", padding=(10, 3, 10, 3), borderwidth=5, relief="raised")

        self.szerokosc_var = tk.StringVar()
        self.wysokosc_var = tk.StringVar()
        self.szerokosc_var.set("2300")
        self.wysokosc_var.set("6000")

        self.szerokosc_label = tk.Label(self.centralwidget, text="Szerokość arkusza:")
        self.szerokosc_label.place(x=330, y=10, width=131, height=22)
        self.szerokosc_entry = tk.Entry(self.centralwidget, textvariable=self.szerokosc_var)
        self.szerokosc_entry.place(x=330, y=40, width=131, height=22)

        self.wysokosc_label = tk.Label(self.centralwidget, text="Wysokość arkusza:")
        self.wysokosc_label.place(x=470, y=10, width=131, height=22)
        self.wysokosc_entry = tk.Entry(self.centralwidget, textvariable=self.wysokosc_var)
        self.wysokosc_entry.place(x=470, y=40, width=131, height=22)

        self.pushButton1 = ttk.Button(self.centralwidget, text="Dodaj", width=70, command=self.dodaj_wiersz)
        self.pushButton1.place(x=20, y=235, width=80, height=28)

        self.pushButton1_2 = ttk.Button(self.centralwidget, text="Zmień", width=70, command=self.zmien_wiersz)
        self.pushButton1_2.place(x=120, y=235, width=80, height=28)

        self.pushButton1_3 = ttk.Button(self.centralwidget, text="Usuń", width=70, command=self.usun_wiersz)
        self.pushButton1_3.place(x=223, y=235, width=80, height=28)

        self.pushButton_generate = ttk.Button(self.centralwidget, text="Generuj", width=70, command=self.generuj_ramki)
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

        frame_size = (46, 120)

        self.frame0 = tk.Canvas(self.groupBox, width=frame_size[0], height=frame_size[1])
        self.frame0.place(x=10, y=20)

        self.frame01 = tk.Canvas(self.groupBox, width=frame_size[0], height=frame_size[1])
        self.frame01.place(x=10 + frame_size[0] + 20, y=20)  # Odsunięcie o 20px na prawo od frame00

        self.lineEdit = tk.Entry(self.centralwidget, width=10)
        self.lineEdit.place(x=25, y=210)

        self.lineEdit_2 = tk.Entry(self.centralwidget, width=10)
        self.lineEdit_2.place(x=95, y=210)

        self.lineEdit_3 = tk.Entry(self.centralwidget, width=10)
        self.lineEdit_3.place(x=165, y=210)

        self.lineEdit_4 = tk.Entry(self.centralwidget, width=10)
        self.lineEdit_4.place(x=235, y=210)

        self.sample_data = [
            ("1", "1000", "2000", "1"),
        ]

        for data in self.sample_data:
            self.tableWidget.insert("", "end", values=data)

        self.tableWidget.bind('<ButtonRelease-1>', self.zaznaczenie_wiersza)

        self.czerwone_ramki = []

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

    def generuj_ramki(self):
        szerokosc_str = self.szerokosc_var.get()
        wysokosc_str = self.wysokosc_var.get()
        rozmiar_combobox = f"{szerokosc_str} x {wysokosc_str}"

        if " x " in rozmiar_combobox:
            szerokosc_str, wysokosc_str = rozmiar_combobox.split(" x ")

            try:
                szerokosc = int(szerokosc_str)
                wysokosc = int(wysokosc_str)

                szerokosc_transformed = szerokosc * 0.02
                wysokosc_transformed = wysokosc * 0.02

                self.frame0.configure(width=int(szerokosc_transformed), height=int(wysokosc_transformed))
                self.frame0.configure(bg="green")

                self.frame01.configure(width=int(szerokosc_transformed), height=int(wysokosc_transformed))
                self.frame01.configure(bg="green")

                ramki = []
                for item in self.tableWidget.get_children():
                    poz, b, h, ilosc = self.tableWidget.item(item, 'values')
                    b = int(b)
                    h = int(h)
                    ilosc = int(ilosc)
                    b_transformed = b * 0.02
                    h_transformed = h * 0.02
                    ramki.append((poz, b_transformed, h_transformed, ilosc))

                for ramka in self.czerwone_ramki:
                    self.frame0.delete(ramka)
                self.czerwone_ramki = []

                obszar_x = 0
                obszar_y = 0
                obszar_szerokosc = int(szerokosc_transformed)
                obszar_wysokosc = int(wysokosc_transformed)

                self.generuj_czerwone_ramki(ramki, obszar_x, obszar_y, obszar_szerokosc, obszar_wysokosc)

            except ValueError:
                print("Niepoprawny format rozmiaru arkusza. Użyj formatu 'szerokość x wysokość' (np. '2300 x 6000').")
        else:
            print("Niepoprawny format rozmiaru arkusza. Użyj formatu 'szerokość x wysokość' (np. '2300 x 6000').")

    def generuj_czerwone_ramki(self, ramki, obszar_x, obszar_y, obszar_szerokosc, obszar_wysokosc):
        ramki.sort(key=lambda x: x[1], reverse=True)

        current_x = obszar_x
        current_y = obszar_y
        current_row_height = 0

        for poz, b, h, ilosc in ramki:
            for _ in range(ilosc):
                if current_x + b <= obszar_x + obszar_szerokosc:
                    frame = self.frame0.create_rectangle(
                        current_x, current_y, current_x + b, current_y + h, fill="red"
                    )
                    self.czerwone_ramki.append(frame)
                    current_x += b
                    current_row_height = max(current_row_height, h)
                else:
                    current_x = obszar_x
                    current_y += current_row_height
                    current_row_height = 0

                if current_x + b > obszar_x + obszar_szerokosc:
                    frame = self.frame01.create_rectangle(
                        current_x - obszar_x - obszar_szerokosc, current_y, current_x - obszar_x - obszar_szerokosc + b, current_y + h, fill="red"
                    )
                    self.czerwone_ramki.append(frame)
                    current_x += b
                    current_row_height = max(current_row_height, h)

if __name__ == "__main__":
    root = tk.Tk()
    app = Ui_MainWindow(root)
    root.mainloop()
