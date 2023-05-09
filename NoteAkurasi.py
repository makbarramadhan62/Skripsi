from prettytable import PrettyTable
import tkinter as tk

table = PrettyTable()

table.add_column("Ekstraksi Fitur", [
                 "RGB & GLCM", "RGB & GLCM2", "HSV & GLCM", "HSV & GLCM2", "HSV", "RGB"])
table.add_column("Akurasi", [0.63, 0.73, 0.78, 0.73, 0.7, 0.63])

print(table)

window = tk.Tk()
window.title("Table")
window.geometry("550x550")

label = tk.Label(window, text=table.get_string().replace(
    '\n', '\n\n'), font=("Courier", 18))
label.pack()

window.mainloop()

# RGB & GLCM = 0.63
# RGB & GLCM2 = 0.73

# HSV & GLCM = 0.78
# HSV & GLCM2 = 0.73

# HSV = 0.7
# RGB = 0.63
