import psutil

def check_ram():
    ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    if ram >= 2:
        return f"RAM: {ram:.2f} GB - Supported"
    else:
        return f"RAM: {ram:.2f} GB - Not Supported"
