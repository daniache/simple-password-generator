import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# Function to generate the password
def generate_password():
    try:
        nr_letters = int(letter_entry.get())
        nr_symbols = int(symbol_entry.get())
        nr_numbers = int(number_entry.get())

        password = generate_password_logic(nr_letters, nr_symbols, nr_numbers)
        
        # Clear previous content and insert the new password
        password_display.delete("1.0", tk.END)
        password_display.insert(tk.END, f"Generated Password: {password}")
        
        check_password_strength(password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Function to create the password
def generate_password_logic(nr_letters, nr_symbols, nr_numbers):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(numbers) for _ in range(nr_numbers)] +
        [random.choice(symbols) for _ in range(nr_symbols)]
    )

    random.shuffle(password_list)
    return ''.join(password_list)

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    strength = "Weak"
    
    if length >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c in "!#$%&()*+" for c in password):
        strength = "Strong"
    elif length >= 6:
        strength = "Medium"
    
    strength_label.config(text=f"Password Strength: {strength}")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_display.get("1.0", tk.END).strip()  # Get all text in the Text widget
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "No password to copy.")

# Setup the tkinter GUI
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.resizable(False, False)

# Use a frame for better layout control
frame = tk.Frame(window, padx=20, pady=20)
frame.pack(expand=True)

# Header
header_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 16, "bold"))
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# Input fields with labels
tk.Label(frame, text="Number of Letters:").grid(row=1, column=0, sticky="e", pady=5)
letter_entry = tk.Entry(frame, width=10)
letter_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Number of Symbols:").grid(row=2, column=0, sticky="e", pady=5)
symbol_entry = tk.Entry(frame, width=10)
symbol_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Number of Numbers:").grid(row=3, column=0, sticky="e", pady=5)
number_entry = tk.Entry(frame, width=10)
number_entry.grid(row=3, column=1, pady=5)

# Generate button
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=("Helvetica", 10, "bold"))
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Password display area using a Text widget with word wrap
password_display = tk.Text(frame, height=4, width=30, wrap="word", font=("Courier", 12))
password_display.grid(row=5, column=0, columnspan=2, pady=10)

# Copy to Clipboard button
copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 10))
copy_button.grid(row=6, column=0, columnspan=2, pady=5)

# Password strength display
strength_label = tk.Label(frame, text="Password Strength: ", font=("Helvetica", 10))
strength_label.grid(row=7, column=0, columnspan=2, pady=5)

# Start the GUI
window.mainloop()
