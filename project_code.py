import os
import subprocess
import tkinter as tk


def grant_permissions(folder_path):
    # Run icacls command to grant permissions to Everyone
    command = f'icacls "{folder_path}" /grant Everyone:(OI)(CI)F'
    subprocess.run(command, shell=True, check=True)

    print(f"Permissions granted to Everyone for folder: {folder_path}")
def on_submit():
    entered_text = entry.get()
    label.config(text=f"Done")
    grant_permissions(entered_text)
    
if __name__ == "__main__":
    
    

    

    
    root = tk.Tk()
    entry = tk.Entry(root, width=30)
    entry.pack()

    
    root.title("My Tkinter Window")

    
    root.geometry("400x300")

    
    label = tk.Label(root, text="Paste the path of your folder ", font=("Helvetica", 16))
    label.pack(pady=20)

    
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()

    
    root.mainloop()

