import whois as python_whois #python-whois
import time
import sys
import os
import warnings
from pathlib import Path
import socket

from utils.utils import isValidDomain, fileExtensionIsSupported

#Usage: python script.py example.com example.org file.txt
def extractValidDomainsFromUserInput(listOfDomainsOrFiles):
    #iterate over user input, if a valid file is found, parse it and append found valid domains to a list of domains.
    #TODO: handle invalid file names, unrecognized file extensions, remove duplicates
    #TODO: Throw an error? warning? Logging?

    listOfValidDomains = []
    supported_files = []
    for domainOrFile in listOfDomainsOrFiles:
        if fileExtensionIsSupported(domainOrFile):
            supported_files.append(domainOrFile)
        elif isValidDomain(domainOrFile):
            listOfValidDomains.append(domainOrFile)
    
    #verify it exists, read it line by line and add non empty lines to the list of  domains
    for supported_file in supported_files:
        if Path(supported_file).is_file():
            with open(supported_file) as f:
                file_domains = [line.strip() for line in f if line.strip() != "" and isValidDomain(line.strip())]
                listOfValidDomains.extend(file_domains)
        else:
            print(f"File {supported_file} does not exist.") 
    return listOfValidDomains

def assingment1(userInputList):
    if len(userInputList) == 0:
        #print(f"Usage: python {scriptFileName} example.com example.org file.txt")
        warnings.warn("Invalid command-line argument/s.", UserWarning)
        return "Invalid command-line argument/s."

    listOfValidDomains = extractValidDomainsFromUserInput(userInputList)
    
    if len(listOfValidDomains) > 0: 
        delay_seconds = 5
        # Set the default socket timeout to 10 seconds
        socket.setdefaulttimeout(10)#TODO: this appears to not work as expected
        for domain in listOfValidDomains:
            try:
                w = python_whois.whois(domain)
                print(f"{domain}: {w.registrar}")
            except socket.timeout:
                print("Operation timed out when querying {domain}: {e}")
            except Exception as e:
                print(f"Error querying {domain}: {e}")
            time.sleep(delay_seconds) #TODO: if last element, do not sleep
        # You can reset the default timeout to None (no timeout) or another value later if needed
        socket.setdefaulttimeout(None)
    else:
        print("Please provide a list of valid domains as a command-line argument and/or a file names ending in .txt.")
        warnings.warn("Invalid command-line argument/s.", UserWarning)
        return "Invalid command-line argument/s."

def main ():
    scriptFileName = sys.argv[0]
    userInputList = sys.argv[1:]
    assingment1(userInputList)

if __name__ == "__main__":
    main()