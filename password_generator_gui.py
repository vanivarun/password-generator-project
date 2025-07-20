import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import sqlite3
from datetime import datetime

# Database setup for saving passwords
def setup_database():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                     (password TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

# Save password to SQLite database
def save_password(password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO passwords (password, timestamp) VALUES (?, ?)", (password, timestamp))
    conn.commit()
    conn.close()

# Retrieve password history
def get_password_history():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password, timestamp FROM passwords ORDER BY timestamp DESC")
    history = cursor.fetchall()
    conn.close()
    return history

# Calculate password strength
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score <= 2:
        return "Weak", "red"
    elif score <= 4:
        return "Moderate", "orange"
    else:
        return "Strong", "green"

# Generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be positive")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number for length")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_special = special_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)
    save_button.config(state="normal")  # Enable save button
    save_button.password = password  # Store password for saving

    # Update strength meter
    strength, color = password_strength(password)
    strength_var.set(f"Strength: {strength}")
    strength_label.config(fg=color)

# Save password action
def save_password_action():
    if hasattr(save_button, 'password'):
        save_password(save_button.password)
        messagebox.showinfo("Success", "Password saved successfully!")
    else:
        messagebox.showerror("Error", "Generate a password first!")

# Copy to clipboard
def copy_to_clipboard():
    if result_var.get():
        pyperclip.copy(result_var.get())
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")

# Show password history
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Password History")
    history_window.geometry("400x300")
    
    tk.Label(history_window, text="Generated Passwords", font=("Arial", 12)).pack(pady=10)
    
    history_frame = tk.Frame(history_window)
    history_frame.pack(fill="both", expand=True)
    
    # Add scrollbar
    canvas = tk.Canvas(history_frame)
    scrollbar = tk.Scrollbar(history_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    history = get_password_history()
    if not history:
        tk.Label(scrollable_frame, text="No passwords saved yet.").pack(pady=5)
    else:
        for pwd, timestamp in history:
            tk.Label(scrollable_frame, text=f"{timestamp}: {pwd}", anchor="w").pack(fill="x", padx=5, pady=2)

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Inputs
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=digit_var).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 14), width=30).pack(pady=10)

# Strength meter
strength_var = tk.StringVar(value="Strength: None")
strength_label = tk.Label(root, textvariable=strength_var, font=("Arial", 10))
strength_label.pack(pady=5)

# Additional buttons
save_button = tk.Button(root, text="Save Password", command=save_password_action, state="disabled")
save_button.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="View Password History", command=show_history).pack(pady=5)

# Initialize database
setup_database()

root.mainloop()