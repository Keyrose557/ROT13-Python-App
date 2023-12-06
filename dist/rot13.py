

import tkinter as tk
from tkinter import scrolledtext

# Function to perform ROT transformation with variable shift
def rot(text, shift, encode=True):
    if not encode:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            alpha_start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - alpha_start + shift) % 26 + alpha_start)
        else:
            result += char
    return result

# Callback using Encode Button
def encode_text():
    transform_text(True)

# Callback using Decode Button
def decode_text():
    transform_text(False)

#  Transformation function
def transform_text(encode):
    input_text = text_area.get("1.0", "end-1c")
    shift_value = shift_scale.get()
    transformed_text = rot(input_text, shift_value, encode)
    text_area.delete("1.0", "end")
    text_area.insert("1.0", transformed_text)

# Main Window
main = tk.Tk()
main.title("ROT Encoder/Decoder")
main.configure(bg="#333333")

# Scalable rows and columns
main.grid_rowconfigure(0, weight=1)
main.grid_rowconfigure(1, weight=0)
main.grid_rowconfigure(2, weight=0)
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)

# Scrollable text widget
text_area = scrolledtext.ScrolledText(main, wrap=tk.WORD, width=40, height=10, font=("Times New Roman", 15), bg="#1e1e1e", fg="white", insertbackground="white")
text_area.grid(column=0, row=0, padx=10, pady=10, columnspan=2, sticky="nsew")

# Scale to select the Shift Value
shift_scale = tk.Scale(main, from_=1, to=25, orient=tk.HORIZONTAL, label="Shift Value", bg="#333333", fg="white")
shift_scale.grid(column=0, row=1, padx=10, pady=10, columnspan=2, sticky="ew")
shift_scale.set(13)  # Default to ROT13

# Trigger to Encode
encode_button = tk.Button(main, text="Encode", command=encode_text, bg="#555555", fg="white")
encode_button.grid(column=0, row=2, padx=10, pady=10, sticky="ew")

# Trigger to Decode
decode_button = tk.Button(main, text="Decode", command=decode_text, bg="#555555", fg="white")
decode_button.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

# Run the application
main.mainloop()
