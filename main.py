import tkinter as tk
from tkinter import ttk
import pyperclip
from art import text2art

def generate_ascii_art():
    word = entry_word.get()
    font_name = combo_font.get()
    ascii_art = text2art(word, font=font_name)
    text_ascii_art.delete(1.0, tk.END)
    text_ascii_art.insert(tk.END, ascii_art)

def copy_to_clipboard():
    ascii_art = text_ascii_art.get(1.0, tk.END)
    pyperclip.copy(ascii_art)

root = tk.Tk()
root.title("ASCII Art Generator")

label_title = tk.Label(root, text="ASCII Art Generator",
                       font=("Helvetica", 25, "bold"),
                       fg='#5e17eb',bg='#E7F9FF')
label_title.place(x=145, y=30)

label_word = tk.Label(root, text="Enter Text:",
                      font=("Helvetica", 12, "bold"),
                      bg='#E7F9FF')
label_word.place(x=170, y=120)

entry_word = tk.Entry(root,font=("Helvetica", 12, "bold"),
                      width=17)
entry_word.place(x=280, y=120)

label_font = tk.Label(root, text="Select Font:",
                      font=("Helvetica", 12, "bold"),
                      bg='#E7F9FF')
label_font.place(x=170, y=170)

fonts = ["block", "bubble", "digital", "ivrit", "mini", "script", "shadow", "smscript", "smshadow",
         "smslant", "standard", "term", "3d", "3x5", "4max", "5lineoblique", "alphabet", "banner",
         "big", "binary", "caligraphy", "chunky", "colossal", "computer", "contessa", "contrast",
         "cosmike", "cyberlarge", "cybermedium", "doh", "doom", "double", "drpepper", "eftirobot",
         "eftitalic", "eftiwall", "eftiwater", "epic", "fender", "fourtops", "fuzzy", "gothic",
         "graffiti", "hex", "hollywood", "invita", "isometric1", "isometric2", "isometric3",
         "isometric4", "italic", "jazmine", "kblock", "larry3d", "lcd", "lean", "letters", "linux",
         "lockergnome", "madrid", "marquee", "maxfour", "merlin1", "merlin2", "mike", "mini",
         "mirror", "mnemonic", "moscow", "mshebrew210", "nancyj", "nancyj-fancy", "nancyj-underlined",
         "ogre", "pacmania", "peaks", "pebbles", "pepper", "poison", "puffy", "rectangles",
         "relief", "relief2", "rev", "roman", "rot13", "rounded", "rowancap", "rozzo", "runic",
         "runyc", "sans", "script", "serifcap", "shadow", "short", "slant", "slide", "slscript",
         "small", "smkeyboard", "smscript", "smshadow", "smslant", "smtengwar", "speed", "stacey",
         "stampate", "standarde", "starwars", "stellar", "stop", "straight", "tanja", "tengwar",
         "term", "thick", "thin", "threepoint", "ticksslant", "tinker-toy", "tombstone", "trek",
         "twopoint", "unifont", "usaflag", "utensil", "wavy", "weird", "wetletter", "whirly", "wow"]

combo_font = ttk.Combobox(root, values=fonts, width=15,
                          font=("Helvetica", 12, "bold"))
combo_font.place(x=280, y=170)

button_generate = tk.Button(root, text="Generate ASCII Art",
                            height='1',width=20,
                            bg='#5e17eb',fg='#E7F9FF',
                            font='Calibri 13 bold',bd=0,
                            command=generate_ascii_art)
button_generate.place(x=210, y=225)

text_ascii_art = tk.Text(root, font=("Courier", 12),
                         bd=0, wrap="word", height=10,
                         width=50)
text_ascii_art.place(x=48, y=270)

button_copy = tk.Button(root, text="Copy to Clipboard",
                        width=20,
                        bg='#5e17eb',fg='#E7F9FF',
                        font='Calibri 13 bold',bd=0,
                        command=copy_to_clipboard)
button_copy.place(x=210, y=470)

insta_page = tk.Label(root, text="@ pythonagham",
                       font=("Helvetica", 10, "bold italic"),
                       fg='#5e17eb',bg='#E7F9FF')
insta_page.place(x=250, y=550)

root.config(bg='#E7F9FF')
root.geometry("600x600")
root.resizable(False, False)
root.mainloop()
