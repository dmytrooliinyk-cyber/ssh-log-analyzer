import csv

def generate_csv_report(suspicious_ips, output_file='incident_report.csv'):
    try:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['IP Address', 'Failed Attempts'])
            
            for ip, count in suspicious_ips.items():
                writer.writerow([ip, count])
        return True
    except Exception:
        return False