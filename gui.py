import tkinter as tk
from tkinter import scrolledtext, ttk
from sniffer import start_sniffing, stop_sniffing
from utils import list_interfaces

def start_capture():
    interface = interface_var.get()
    if interface:
        log_text.insert(tk.END, f"[INFO] Starting Sniffing on {interface}...\n")
        start_sniffing(interface)

def stop_capture():
    stop_sniffing()
    log_text.insert(tk.END, "[INFO] Stopping Sniffing...\n")

def start_gui():
    global log_text, interface_var

    root = tk.Tk()
    root.title("Wireless Packet Sniffer - File Upload Detector")
    root.geometry("600x400")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="Select Interface:").grid(row=0, column=0, padx=10)
    interface_var = ttk.Combobox(frame, values=list_interfaces())
    interface_var.grid(row=0, column=1, padx=10)
    interface_var.current(0)

    start_button = tk.Button(frame, text="Start Sniffing", command=start_capture, bg="green", fg="white")
    start_button.grid(row=1, column=0, padx=10)

    stop_button = tk.Button(frame, text="Stop Sniffing", command=stop_capture, bg="red", fg="white")
    stop_button.grid(row=1, column=1, padx=10)

    log_text = scrolledtext.ScrolledText(root, width=70, height=15)
    log_text.pack(pady=10)

    root.mainloop()
