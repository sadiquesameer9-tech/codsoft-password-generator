import tkinter as tk
from tkinter import messagebox
import random
import string


# ==========================================
# GENERATE PASSWORD FUNCTION
# ==========================================

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Invalid Length",
                "Password length must be at least 4."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )
        return

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Get selected complexity
    complexity = complexity_var.get()

    if complexity == 1:
        characters = lowercase

    elif complexity == 2:
        characters = lowercase + uppercase

    elif complexity == 3:
        characters = lowercase + uppercase + numbers

    elif complexity == 4:
        characters = lowercase + uppercase + numbers + special

    else:
        messagebox.showwarning(
            "Select Complexity",
            "Please select a password complexity."
        )
        return

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    # Display password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ==========================================
# COPY PASSWORD
# ==========================================

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Please generate a password first."
        )
        return

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )


# ==========================================
# CLEAR FUNCTION
# ==========================================

def clear_all():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    complexity_var.set(0)


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("Password Generator")
window.geometry("650x550")
window.resizable(False, False)
window.configure(bg="#1e1e2f")


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    window,
    text="PASSWORD GENERATOR",
    font=("Arial", 28, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title.pack(pady=(35, 10))


subtitle = tk.Label(
    window,
    text="Create a strong and random password",
    font=("Arial", 13),
    bg="#1e1e2f",
    fg="#b8b8c7"
)

subtitle.pack(pady=(0, 30))


# ==========================================
# PASSWORD LENGTH
# ==========================================

length_label = tk.Label(
    window,
    text="Password Length",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="white"
)

length_label.pack()


length_entry = tk.Entry(
    window,
    font=("Arial", 16),
    justify="center",
    width=15,
    bg="#2b2b40",
    fg="white",
    insertbackground="white",
    relief="flat"
)

length_entry.pack(pady=10)

length_entry.insert(0, "12")


# ==========================================
# COMPLEXITY
# ==========================================

complexity_label = tk.Label(
    window,
    text="Password Complexity",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="white"
)

complexity_label.pack(pady=(15, 8))


complexity_var = tk.IntVar(value=4)


# Lowercase
radio1 = tk.Radiobutton(
    window,
    text="Lowercase Letters",
    variable=complexity_var,
    value=1,
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="white",
    selectcolor="#2b2b40",
    activebackground="#1e1e2f",
    activeforeground="white"
)

radio1.pack()


# Uppercase
radio2 = tk.Radiobutton(
    window,
    text="Lowercase + Uppercase",
    variable=complexity_var,
    value=2,
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="white",
    selectcolor="#2b2b40",
    activebackground="#1e1e2f",
    activeforeground="white"
)

radio2.pack()


# Numbers
radio3 = tk.Radiobutton(
    window,
    text="Letters + Numbers",
    variable=complexity_var,
    value=3,
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="white",
    selectcolor="#2b2b40",
    activebackground="#1e1e2f",
    activeforeground="white"
)

radio3.pack()


# Special characters
radio4 = tk.Radiobutton(
    window,
    text="Letters + Numbers + Special Characters",
    variable=complexity_var,
    value=4,
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="white",
    selectcolor="#2b2b40",
    activebackground="#1e1e2f",
    activeforeground="white"
)

radio4.pack()


# ==========================================
# GENERATE BUTTON
# ==========================================

generate_button = tk.Button(
    window,
    text="GENERATE PASSWORD",
    command=generate_password,
    font=("Arial", 13, "bold"),
    bg="#4a90e2",
    fg="white",
    activebackground="#357abd",
    activeforeground="white",
    relief="flat",
    width=22,
    height=2,
    cursor="hand2"
)

generate_button.pack(pady=20)


# ==========================================
# PASSWORD DISPLAY
# ==========================================

password_entry = tk.Entry(
    window,
    font=("Arial", 16, "bold"),
    justify="center",
    width=35,
    bg="#2b2b40",
    fg="#00ff99",
    insertbackground="white",
    relief="flat"
)

password_entry.pack(pady=5)


# ==========================================
# BUTTON FRAME
# ==========================================

button_frame = tk.Frame(
    window,
    bg="#1e1e2f"
)

button_frame.pack(pady=15)


# COPY BUTTON
copy_button = tk.Button(
    button_frame,
    text="COPY",
    command=copy_password,
    font=("Arial", 11, "bold"),
    bg="#27ae60",
    fg="white",
    activebackground="#219150",
    relief="flat",
    width=10,
    height=1,
    cursor="hand2"
)

copy_button.grid(row=0, column=0, padx=8)


# CLEAR BUTTON
clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_all,
    font=("Arial", 11, "bold"),
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    relief="flat",
    width=10,
    height=1,
    cursor="hand2"
)

clear_button.grid(row=0, column=1, padx=8)


# ==========================================
# RUN APPLICATION
# ==========================================

window.mainloop()
