import tkinter as tk
from tkinter import ttk
import customtkinter as ctk




#------------ WIndow ----------------
window = tk.Tk()
window.title('Character Helper:')
window.geometry('1101x783')

#------------ Top/Header ----------------
header = tk.Frame(master=window)
#header 1
h1_frame = tk.Frame(master=header)
h1 = tk.Label(master = h1_frame, text='Character Helper')
#header 2
h2_frame = tk.Frame(master=header)
h2_string = tk.StringVar() # will contain this '{} {} Level:{}'.format(char_name, char_class, char_level) char_level as int
h2 = tk.Label(master = header, text="[] [] Level:[]",textvariable=h2_string)

#Tabs:
tab_frame = tk.Frame(master=header)
character1_string = ctk.StringVar()
character1 = ctk.CTkButton(master=tab_frame, textvariable= character1_string, corner_radius=20)

character2_string = ctk.StringVar()
character2 = ctk.CTkButton(master=tab_frame, textvariable= character2_string, corner_radius=20)

character3_string = ctk.StringVar()
character3 = ctk.CTkButton(master=tab_frame, textvariable= character3_string, corner_radius=20)

character4_string = ctk.StringVar()
character4 = ctk.CTkButton(master=tab_frame, textvariable= character4_string, corner_radius=20)

#Pack frames:
header.pack(), h1_frame.pack(), h2_frame.pack(), tab_frame.pack(side='right')
#Pack Labels:
h1.pack(), h2.pack(), character1.pack(side='right', padx=5),character2.pack(side='right', padx=5),character3.pack(side='right', padx=5),character4.pack(side='right', padx=5)
#------------ run ----------------
window.mainloop()