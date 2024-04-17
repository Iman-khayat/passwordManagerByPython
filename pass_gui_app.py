import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def generate_key():
   return Fernet.generate_key()

# Encrypt the password
def encrypt_password(password, key):
        cipher_suite = Fernet(key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password, key):
        cipher_suite = Fernet(key)
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password
# Save encrypted password to a file
def save_password(website, username, encrypted_password):
    key = generate_key()
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as file:
        file.write(f"{website},{username},{encrypted_password.decode()}\n")



    messagebox.showinfo("Password Manager", f"Password for {website} saved successfully!")


# Create main window
root = tk.Tk()
root.title("Password Manager")

# Create labels
website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Create entry fields
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=10, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Create save button
save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
