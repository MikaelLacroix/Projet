import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import fonctions

# List of cipher methods
encodage = ["","Caesar", "Caesar Incremental", "Vigenere"]

def frame1(root):
    frame1 = tk.Frame(root, bg="lightblue", width=1920, height=1080)
    l1 = ttk.Label(frame1, text="Texte en clair :")
    l1.place(x=175, y=20)
    inputtxt = tk.Text(frame1, height=10, width=40)
    inputtxt.place(x=50, y=50)
    l2 = ttk.Label(frame1, text="Texte chiffre :")
    l2.place(x=725, y=20)
    l3 = ttk.Label(frame1, text="Fonction de chiffrage :")
    l3.place(x=175, y=310)
    l4 = ttk.Label(frame1, text="Nombre de decalage :")
    l4.place(x=175, y=340)

    selected_encodage = tk.StringVar(value=encodage[0])
    scrollmenu = ttk.OptionMenu(frame1, selected_encodage, *encodage)
    scrollmenu.place(x=450, y=310)

    e1 = ttk.Entry(frame1)
    e1.place(x=450, y=340)

    inputtxt1 = tk.Text(frame1, height=10, width=40)
    inputtxt1.place(x=600, y=50)

    def encode_button_click():
        fonctions.encodage_caesar(inputtxt, selected_encodage, inputtxt1, e1, tk)

    def decode_button_click():
        fonctions.decodage_caesar(inputtxt1, selected_encodage, inputtxt, e1, tk)

    b1 = ttk.Button(frame1, text="=> Encoder =>", command=encode_button_click)
    b1.place(x=450, y=90)

    b2 = ttk.Button(frame1, text="<= Décoder <=", command=decode_button_click)
    b2.place(x=450, y=130)

    frame1.pack_propagate(False)
    frame1.pack(fill="both", expand=True)

    return frame1

def frame2(root):
    frame2 = tk.Frame(root, bg="lightgreen", width=1920, height=1080)
    l5 = ttk.Label(frame2, text="Texte en clair :")
    l5.place(x=175, y=20)
    l6 = ttk.Label(frame2, text="Texte chiffre :")
    l6.place(x=725, y=20)
    l7 = ttk.Label(frame2, text="Fonction de chiffrage :")
    l7.place(x=175, y=310)
    l8 = ttk.Label(frame2, text="Nombre de decalage :")
    l8.place(x=175, y=340)
    def encode_button_click():
        fonctions.encodage_caesar(inputtxt, selected_encodage, inputtxt1, e1, tk)

    def decode_button_click():
        fonctions.decodage_caesar(inputtxt1, selected_encodage, inputtxt, e1, tk)

    b5 = ttk.Button(frame2, text="=> Encoder =>", command=encode_button_click)
    b5.place(x=450, y=90)
    b6 = ttk.Button(frame2, text="<= Décoder <=", command=decode_button_click)
    b6.place(x=450, y=130)
    b7 = ttk.Button(frame2, text="Ouvrir un fichier", command=lambda: fonctions.ouverture_fichier(inputtxt, tk))
    b7.place(x=175, y=225)
    e1 = ttk.Entry(frame2)
    e1.place(x=450, y=340)
    inputtxt = tk.Text(frame2, height=10, width=40)
    inputtxt.place(x=50, y=50)
    inputtxt1 = tk.Text(frame2, height=10, width=40)
    inputtxt1.place(x=600, y=50)
    selected_encodage = tk.StringVar(value=encodage[0])
    scrollmenu1 = ttk.OptionMenu(frame2, selected_encodage, *encodage)
    scrollmenu1.place(x=450, y=310)
    frame2.pack_propagate(False)
    frame2.pack(fill="both", expand=True)
    return frame2

def frame3(root):
    def encode_web_content():
        url = e1.get()
        css_selector = e2.get()
        cipher_method = selected_encodage.get()
        shift = e3.get()
        
        encoded_text = fonctions.web_content_cipher(url, css_selector, cipher_method, shift)
        if encoded_text:
            inputtxt1.delete("1.0", tk.END)
            inputtxt1.insert(tk.END, encoded_text)
        else:
            messagebox.showerror("Error", "Failed to encode web content.")
    
    def decode_web_content():
        url = e1.get()
        css_selector = e2.get()
        cipher_method = selected_encodage.get()
        shift = e3.get()
        
        decoded_text = fonctions.web_content_decipher(url, css_selector, cipher_method, shift)
        if decoded_text:
            inputtxt1.delete("1.0", tk.END)
            inputtxt1.insert(tk.END, decoded_text)
        else:
            messagebox.showerror("Error", "Failed to decode web content.")
    
    frame3 = tk.Frame(root, bg="pink", width=1920, height=1080)
    l9 = ttk.Label(frame3, text="URL, et sélecteur :")
    l9.place(x=20, y=10)
    l10 = ttk.Label(frame3, text="Fonction de chiffrement :")
    l10.place(x=0, y=255)
    l11 = ttk.Label(frame3, text="Nombre de décalage :")
    l11.place(x=0, y=280)
    l12 = ttk.Label(frame3, text="Texte Résultat :")
    l12.place(x=385, y=10)
    e1 = ttk.Entry(frame3)
    e1.place(x=0, y=80)
    e2 = ttk.Entry(frame3)
    e2.place(x=0, y=150)
    e3 = ttk.Entry(frame3)
    e3.place(x=135, y=280)
    b1 = ttk.Button(frame3, text=" => Encoder =>", command=encode_web_content)
    b1.place(x=150, y=80)
    b2 = ttk.Button(frame3, text=" => Decoder =>", command=decode_web_content)
    b2.place(x=150, y=150)
    selected_encodage = tk.StringVar(value=encodage[0])
    scrollmenu1 = ttk.OptionMenu(frame3, selected_encodage, *encodage)
    scrollmenu1.place(x=150, y=255)
    inputtxt1 = tk.Text(frame3, height=10, width=40)
    inputtxt1.place(x=275, y=40)
    frame3.pack_propagate(False)
    frame3.pack(fill="both", expand=True)
    return frame3

def show_frame1():
    global current_frame
    if current_frame:
        current_frame.pack_forget()
    current_frame = frame1(root)

def show_frame2():
    global current_frame
    if current_frame:
        current_frame.pack_forget()
    current_frame = frame2(root)

def show_frame3():
    global current_frame
    if current_frame:
        current_frame.pack_forget()
    current_frame = frame3(root)

root = tk.Tk()
root.title("Encoding application")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a menu
menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Chiffrage de texte", command=show_frame1)
menu_bar.add_cascade(label="Chiffrage de Fichier", command=show_frame2)
menu_bar.add_cascade(label="Chiffrage de contenu web", command=show_frame3)
menu_bar.add_command(label="Fermer", command=root.quit)

# Initialize current_frame
current_frame = None
show_frame1()

root.mainloop()

