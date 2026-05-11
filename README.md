SSH Log Analyzer and Brute-Force Detector



Project Overview

This project is a Python tool I wrote to analyze standard Linux authentication logs ('auth.log'). Its main goal is to find potential SSH brute-force attacks. The script reads the logs, extracts the IP addresses that failed to log in, counts how many times they tried, and flags them if they cross a specific threshold. It then saves everything into a neat CSV report.



How the code is structured

I divided the script into separate modules to keep the code clean:



'main.py' is the main file that runs the whole process.



'parser.py' handles reading the file and uses regular expressions to pick out the IP addresses.



'analyzer.py' does the counting and checks if an IP crossed the allowed limit.



'report.py' takes the final data and creates the 'incident\_report.csv' file.



How to run it

To use this tool, just download the project and make sure you have an 'auth.log' file inside a 'logs' folder.

Open your terminal, navigate to the folder, and type: python main.py

If the script finds any suspicious activity, it will print a message to the console and create the CSV file with the results.



Next steps

Later on, I plan to connect this tool to the AbuseIPDB API to automatically check if the suspicious IPs are known hackers. I also want to add a check for successful logins that happen immediately after multiple failed attempts.

