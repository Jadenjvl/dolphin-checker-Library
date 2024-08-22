import cpuinfo

def check_cpu():
    cpu_info = cpuinfo.get_cpu_info()
    if cpu_info['bits'] == 64 and cpu_info['hz_actual_friendly']:
        return f"CPU: {cpu_info['brand_raw']} ({cpu_info['hz_actual_friendly']}) - Supported"
    else:
        return f"CPU: {cpu_info['brand_raw']} ({cpu_info['hz_actual_friendly']}) - Not Supported"
