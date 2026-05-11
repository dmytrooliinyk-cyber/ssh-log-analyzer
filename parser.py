import re

def extract_failed_ips(log_path):
    failed_ips = []
    regex_pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"
    
    try:
        with open(log_path, 'r') as file:
            for line in file:
                match = re.search(regex_pattern, line)
                if match:
                    failed_ips.append(match.group(1))
        return failed_ips
    except FileNotFoundError:
        return None