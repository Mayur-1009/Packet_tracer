import pyshark
import threading
from notifier import send_alert
from utils import enable_monitor_mode, list_interfaces

running = False
selected_interface = "eth0"  # Default to wired

def packet_sniffer():
    global running, selected_interface

    # Enable monitor mode if wireless
    if "wlan" in selected_interface or "mon" in selected_interface:
        enable_monitor_mode(selected_interface)

    # Define capture filter
    capture = pyshark.LiveCapture(interface=selected_interface, display_filter="http or ftp or wlan")

    for packet in capture:
        if not running:
            break
        try:
            if "HTTP" in packet and hasattr(packet.http, "request_method"):
                if packet.http.request_method == "POST" and "multipart/form-data" in packet.http.content_type:
                    alert_msg = f"[ALERT] File Upload Detected on {packet.http.host}"
                    send_alert(alert_msg)
            elif "FTP" in packet:
                alert_msg = f"[ALERT] FTP Upload Detected on {packet.ip.dst}"
                send_alert(alert_msg)
            elif "WLAN" in packet and hasattr(packet, "wlan_radio"):
                alert_msg = f"[INFO] Wireless Packet Detected from {packet.wlan.sa} to {packet.wlan.da}"
                send_alert(alert_msg)
        except AttributeError:
            continue

def start_sniffing(interface):
    global running, selected_interface
    selected_interface = interface
    running = True
    thread = threading.Thread(target=packet_sniffer, daemon=True)
    thread.start()

def stop_sniffing():
    global running
    running = False
