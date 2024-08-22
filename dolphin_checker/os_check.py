import platform

def check_os():
    os_name = platform.system()
    if os_name in ["Windows", "Darwin", "Linux"]:
        return f"Operating System: {os_name} - Supported"
    else:
        return f"Operating System: {os_name} - Not Supported"
