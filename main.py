import parser
import analyzer
import report

def main():
    log_file_path = 'logs/auth.log'
    threshold = 3 
    
    ips = parser.extract_failed_ips(log_file_path)
    
    if ips is None:
        print("Error: Log file not found.")
        return
        
    suspicious_activity = analyzer.detect_brute_force(ips, threshold)
    
    if not suspicious_activity:
        print("No brute-force activity detected.")
        return
        
    print(f"Detected {len(suspicious_activity)} suspicious IPs.")
    
    success = report.generate_csv_report(suspicious_activity)
    
    if success:
        print("Report successfully generated: incident_report.csv")
    else:
        print("Failed to generate report.")

if __name__ == "__main__":
    main()