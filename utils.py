import subprocess

def enable_monitor_mode(interface):
    """ Enable monitor mode for wireless sniffing. """
    try:
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        subprocess.run(["sudo", "iwconfig", interface, "mode", "monitor"], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(f"[INFO] Enabled monitor mode on {interface}")
    except Exception as e:
        print(f"[ERROR] Failed to enable monitor mode: {e}")

def list_interfaces():
    """ List available network interfaces. """
    try:
        result = subprocess.run(["ip", "link", "show"], capture_output=True, text=True)
        interfaces = [line.split(": ")[1] for line in result.stdout.split("\n") if ": " in line]
        return interfaces
    except Exception as e:
        print(f"[ERROR] Failed to list interfaces: {e}")
        return ["wlan0", "wlan1", "mon0", "eth0", "lo"]
