from collections import Counter

def detect_brute_force(ip_list, threshold=5):
    ip_counts = Counter(ip_list)
    suspicious_ips = {}
    
    for ip, count in ip_counts.items():
        if count >= threshold:
            suspicious_ips[ip] = count
            
    return suspicious_ips