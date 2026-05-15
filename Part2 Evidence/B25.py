import re

# Local threat intelligence database
threat_db = {
    "185.220.101.1": {
        "type": "Malicious IP",
        "risk": "High",
        "description": "Known Tor exit node commonly used for anonymous suspicious traffic.",
        "action": "Block IP and investigate related logs."
    },
    "malicious-login.com": {
        "type": "Phishing Domain",
        "risk": "Critical",
        "description": "Domain associated with fake login pages.",
        "action": "Block domain and warn users."
    },
    "http://badsite.com/free-login": {
        "type": "Malicious URL",
        "risk": "High",
        "description": "URL linked to credential harvesting.",
        "action": "Block URL using web filtering."
    },
    "44d88612fea8a8f36de82e1278abb02f": {
        "type": "Malware Hash",
        "risk": "Critical",
        "description": "Hash associated with malware sample.",
        "action": "Quarantine file and scan affected host."
    }
}

def identify_ioc(ioc):
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ioc):
        return "IP Address"
    elif re.match(r"^https?://", ioc):
        return "URL"
    elif re.match(r"^[a-fA-F0-9]{32,64}$", ioc):
        return "File Hash"
    elif "." in ioc:
        return "Domain"
    else:
        return "Unknown"

def check_ioc(ioc):
    ioc = ioc.strip().lower()
    ioc_type = identify_ioc(ioc)

    print("\n--- Threat Intelligence Result ---")
    print(f"IOC: {ioc}")
    print(f"IOC Type: {ioc_type}")

    if ioc in threat_db:
        result = threat_db[ioc]
        print(f"Threat Type: {result['type']}")
        print(f"Risk Level: {result['risk']}")
        print(f"Description: {result['description']}")
        print(f"Recommended Action: {result['action']}")
    else:
        print("Threat Status: Unknown")
        print("Risk Level: Low/Unknown")
        print("Recommended Action: Monitor and investigate if repeated activity is detected.")

def main():
    print("Threat Intelligence IOC Checker")
    print("Enter an IP, domain, URL, or file hash.")
    print("Type 'exit' to quit.")

    while True:
        ioc = input("\nEnter IOC: ")

        if ioc.lower() == "exit":
            print("Exiting threat intelligence module.")
            break

        check_ioc(ioc)

if __name__ == "__main__":
    main()