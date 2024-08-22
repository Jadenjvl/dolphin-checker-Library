import platform
import subprocess

def check_gpu():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic path win32_videocontroller get caption", shell=True).decode()
            gpus = output.splitlines()[1:]
            gpu_info = ', '.join(gpu.strip() for gpu in gpus if gpu.strip())
            return f"GPU: {gpu_info} - Check if it supports OpenGL 3.0/DirectX 11"
        elif platform.system() == "Linux":
            output = subprocess.check_output("lspci | grep VGA", shell=True).decode()
            gpu_info = output.strip()
            return f"GPU: {gpu_info} - Check if it supports OpenGL 3.0/DirectX 11"
        elif platform.system() == "Darwin":
            output = subprocess.check_output("system_profiler SPDisplaysDataType | grep 'Chipset Model'", shell=True).decode()
            gpu_info = output.strip().split(": ")[1]
            return f"GPU: {gpu_info} - Check if it supports OpenGL 3.0/DirectX 11"
        else:
            return "GPU: Not Supported"
    except subprocess.CalledProcessError:
        return "GPU: Unable to determine - Not Supported"
