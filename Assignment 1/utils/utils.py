def isValidDomain(domain):
    #TODO: implement a proper domain validation
    #basic validation, can be improved
    if "." in domain and " " not in domain:
        return True
    else: 
        print(f"Invalid domain: {domain}")
    return False

def fileExtensionIsSupported(fileName):
    supportedExtensions = [".txt"] #TODO: add more supported file extensions
    for ext in supportedExtensions:
        if fileName.endswith(ext):
            return True
    return False