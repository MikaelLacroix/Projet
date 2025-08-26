import string
import tkinter as tk
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup

def get_web_content(url, css_selector):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            selected_element = soup.select_one(css_selector)
            if selected_element:
                return selected_element.get_text()
            else:
                return "No element found with the provided CSS selector."
        else:
            return "Failed to retrieve content from the URL."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def web_content_cipher(url, css_selector, cipher_method, shift=None, key=None):
    content = get_web_content(url, css_selector)
    if content:
        if cipher_method == "Caesar":
            if shift is None:
                return "Shift value is required for Caesar cipher."
            try:
                shift = int(shift) % 26
                return caesar_cipher(content, shift)
            except ValueError:
                return "Invalid shift value for Caesar cipher."
        elif cipher_method == "Caesar Incremental":
            if shift is None:
                return "Initial shift value is required for Caesar Incremental cipher."
            try:
                shift = int(shift)
                return caesar_incremental_encode(content, shift)
            except ValueError:
                return "Invalid initial shift value for Caesar Incremental cipher."
        elif cipher_method == "Vigenere":
            if key is None:
                return "Key is required for Vigenere cipher."
            return vigenere_cipher(content, key)
        else:
            return "Unsupported cipher method."
    else:
        return "Failed to retrieve content for encryption/decryption."

def web_content_decipher(url, css_selector, cipher_method, shift=None, key=None):
    content = get_web_content(url, css_selector)
    if content:
        if cipher_method == "Caesar":
            if shift is None:
                return "Shift value is required for Caesar cipher."
            try:
                shift = int(shift) % 26
                return caesar_cipher(content, -shift)
            except ValueError:
                return "Invalid shift value for Caesar cipher."
        elif cipher_method == "Caesar Incremental":
            if shift is None:
                return "Initial shift value is required for Caesar Incremental cipher."
            try:
                shift = int(shift)
                return caesar_incremental_decode(content, shift)
            except ValueError:
                return "Invalid initial shift value for Caesar Incremental cipher."
        elif cipher_method == "Vigenere":
            if key is None:
                return "Key is required for Vigenere cipher."
            return vigenere_cipher(content, key, decrypt=True)
        else:
            return "Unsupported cipher method."
    else:
        return "Failed to retrieve content for encryption/decryption."


def ouverture_fichier(inputtxt, tk):
    file_path = filedialog.askopenfilename(title="Ouvrir un fichier", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:
        with open(file_path, 'r') as file:
            data = file.read()
            inputtxt.delete(1.0, tk.END)
            inputtxt.insert(tk.END, data)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result


def caesar_incremental_encode(plaintext, initial_shift):
    ciphertext = ""
    shift = initial_shift
    for char in plaintext:
        if char.isalpha():
            # S'assure que shift va enlentour de la plage alphabétique
            shift = shift % 26
            ciphertext += caesar_cipher(char, shift)
            shift += 1
        else:
            ciphertext += char
    return ciphertext

def caesar_incremental_decode(ciphertext, initial_shift):
    plaintext = ""
    shift = initial_shift
    for char in ciphertext:
        if char.isalpha():
            # S'assure que shift va enlentour de la plage alphabétique
            shift = shift % 26
            plaintext += caesar_cipher(char, -shift)
            shift += 1
        else:
            plaintext += char
    return plaintext

def vigenere_cipher(text, key, decrypt=False):
    text = text.upper()
    key = key.upper()
    key_len = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    key_repeat = key_len * (len(text) // key_len) + key_len
    key_as_int *= len(text) // key_len
    key_as_int += key_as_int[:len(text) % key_len]
    
    if decrypt:
        key_as_int = [-k for k in key_as_int]
    
    encrypted = [chr((t + k) % 26 + ord('A')) if t != ord(' ') else ' ' for t, k in zip(text_as_int, key_as_int)]
    
    return ''.join(encrypted)

def encodage_caesar(inputtxt, selected_encodage, outputtxt, e1, tk):
    selected_cipher = selected_encodage.get()
    text_to_encode = inputtxt.get("1.0", tk.END).strip()
    
    if selected_cipher == "Caesar":
        try:
            selected_shift = int(e1.get()) % 26  # S'assure que shift est dans la plage alphabétique
            encoded_text = caesar_cipher(text_to_encode, selected_shift)
        except ValueError:
            encoded_text = "Invalid shift value"
    elif selected_cipher == "Caesar Incremental":
        try:
            selected_shift = int(e1.get())
            encoded_text = caesar_incremental_encode(text_to_encode, selected_shift)
        except ValueError:
            encoded_text = "Invalid shift value"
    elif selected_cipher == "Vigenere":
        vigenere_key = e1.get().upper()
        encoded_text = vigenere_cipher(text_to_encode, vigenere_key)
    else:
        encoded_text = "Unsupported cipher"
    
    inputtxt.delete("1.0", tk.END)
    outputtxt.delete("1.0", tk.END)
    outputtxt.insert(tk.END, encoded_text)

def decodage_caesar(inputtxt, selected_encodage, outputtxt, e1, tk):
    selected_cipher = selected_encodage.get()
    text_to_decode = inputtxt.get("1.0", tk.END).strip()
    
    if selected_cipher == "Caesar":
        try:
            selected_shift = int(e1.get()) % 26  # S'assure que shift est dans la plage alphabétique
            decoded_text = caesar_cipher(text_to_decode, -selected_shift)
        except ValueError:
            decoded_text = "Invalid shift value"
    elif selected_cipher == "Caesar Incremental":
        try:
            selected_shift = int(e1.get())
            decoded_text = caesar_incremental_decode(text_to_decode, selected_shift)
        except ValueError:
            decoded_text = "Invalid shift value"
    elif selected_cipher == "Vigenere":
        vigenere_key = e1.get().upper()
        decoded_text = vigenere_cipher(text_to_decode, vigenere_key, decrypt=True)
    else:
        decoded_text = "Unsupported cipher"
    
    inputtxt.delete("1.0", tk.END)
    outputtxt.delete("1.0", tk.END)
    outputtxt.insert(tk.END, decoded_text)

def get_web_content(url, css_selector):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            selected_elements = soup.select(css_selector)
            extracted_text = [element.get_text() for element in selected_elements]
            return "\n".join(extracted_text)
        else:
            return "Failed to retrieve content from the URL."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Encoding function for web content
def web_content_cipher(url, css_selector, cipher_method, shift=None, key=None):
    content = get_web_content(url, css_selector)
    if content:
        if cipher_method == "Caesar":
            if shift is None:
                return "Un atribuer shift doit etre la pour le cipher a caesar"
            try:
                shift = int(shift) % 26
                return caesar_cipher(content, shift)
            except ValueError:
                return "shift invlaide."
        elif cipher_method == "Caesar Incremental":
            if shift is None:
                return "Un atribuer shift doit etre la pour le cipher a caesar"
            try:
                shift = int(shift)
                return caesar_incremental_encode(content, shift)
            except ValueError:
                return "Un atribuer shift doit etre la pour le cipher a caesar"
        elif cipher_method == "Vigenere":
            if key is None:
                return "Key is required for Vigenere cipher."
            return vigenere_cipher(content, key)
        else:
            return "Unsupported cipher method."
    else:
        return "encryption/decryption marche pas."

# Decoding function for web content
def web_content_decipher(url, css_selector, cipher_method, shift=None, key=None):
    content = get_web_content(url, css_selector)
    if content:
        if cipher_method == "Caesar":
            if shift is None:
                return "Un atribuer shift doit etre la pour le cipher a caesar"
            try:
                shift = int(shift) % 26
                return caesar_cipher(content, -shift)
            except ValueError:
                return "Invalid atribuer  pour le cipher a caesar"
        elif cipher_method == "Caesar Incremental":
            if shift is None:
                return "Un atribuer shift doit etre la pour le cipher a caesar."
            try:
                shift = int(shift)
                return caesar_incremental_decode(content, shift)
            except ValueError:
                return "Un atribuer shift doit etre la pour le cipher a caesar"
        elif cipher_method == "Vigenere":
            if key is None:
                return "un numero cle doit etre dans le code pour qui se fait encrypter."
            return vigenere_cipher(content, key, decrypt=True)
        else:
            return "Unsupported cipher method."
    else:
        return "encryption/decryption marche pas."

