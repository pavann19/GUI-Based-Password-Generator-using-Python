import random
import string
import tkinter as tk
from tkinter import simpledialog

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        
        self.password_data = {}  # Store app names and passwords
        
        # Customize background colors
        entry_bg_color = "#F0F0F0"  # Light gray
        button_bg_color = "#4CAF50"  # Green
        
        self.app_name_label = tk.Label(root, text="App Name:", font=("Helvetica", 12))
        self.app_name_label.pack(pady=10)
        
        self.app_name_entry = tk.Entry(root, bg=entry_bg_color, font=("Helvetica", 12))
        self.app_name_entry.pack(pady=5)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg=button_bg_color, font=("Helvetica", 12))
        self.generate_button.pack(pady=5)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit, bg=button_bg_color, font=("Helvetica", 12))
        self.quit_button.pack(pady=10)
        
    def generate_password(self):
        app_name = self.app_name_entry.get()
        
        if app_name:
            password = generate_strong_password()
            self.password_data[app_name] = password
            
            message = f"Password for {app_name}:\n{password}"
            simpledialog.messagebox.showinfo("Generated Password", message)
            
            self.app_name_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry("300x200")
    app = PasswordManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
