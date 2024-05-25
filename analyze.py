# Author: Uphar Jaiswal

import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check for minimum length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

def analyze_password():
    password = entry.get()
    strength, feedback = check_password_strength(password)
    
    if strength == 4:
        messagebox.showinfo("Password Strength", "Your password is strong!")
    else:
        messagebox.showwarning("Password Strength", "\n".join(feedback))

# Set up the GUI window
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("450x350")
root.resizable(True, True)

# Create GUI components
label = tk.Label(root, text="Enter your password:")
label.pack(pady=15)

entry = tk.Entry(root, show="*", width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Analyze Password", command=analyze_password)
button.pack(pady=10)

# Run the GUI loop
root.mainloop()