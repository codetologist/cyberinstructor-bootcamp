import whois #python-whois
import time
import sys
import os
from pathlib import Path

#Usage: python script.py example.com example.org file.txt

def isValidDomain(domain):
    #TODO: implement a proper domain validation
    #basic validation, can be improved
    if "." in domain and " " not in domain:
        return True
    else: 
        print(f"Invalid domain: {domain}")
    return False

if __name__ == "__main__":
    scriptFileName = os.path.basename(__file__) #same as using sys.argv[0]
    domains = [domain for domain in sys.argv if domain != "" and domain != scriptFileName] #exclude script name and empty strings
    
    #iterate over domains, if a string ends with .txt append it to a list of files
    txt_files = []
    for domain in domains:
        if domain.endswith(".txt"):
            txt_files.append(domain)
    
    #verify it exists, read it line by line and add non empty lines to the list of  domains
    for txt_file in txt_files:
        if Path(txt_file).is_file():
            with open(txt_file) as f:
                file_domains = [line.strip() for line in f if line.strip() != "" and isValidDomain(line.strip())]
                domains.extend(file_domains)
            domains.remove(txt_file) #remove the file name from the list of domains
        else:
            print(f"File {txt_file} does not exist.")
            domains.remove(txt_file) #remove the non-existent file name from the list of domains

    if len(domains) > 0: 
        delay_seconds = 5
        for domain in domains:
            try:
                w = whois.whois(domain)
                print(f"{domain}: {w.registrar}")
            except Exception as e:
                print(f"Error querying {domain}: {e}")
            time.sleep(delay_seconds)
    else:
        print("Please provide a list of domains as a command-line argument and/or a file names ending in .txt.")