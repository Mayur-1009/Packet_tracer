import tkinter.messagebox as messagebox

def send_alert(message):
    print(message)  # Console log
    messagebox.showwarning("File Upload Alert", message)
