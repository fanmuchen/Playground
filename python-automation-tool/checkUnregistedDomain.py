import whois

# List of .ai domains to check
domains = [
    "fmc.ai",
    "law.ai",
    "example3.ai",
    "example4.ai"
]

# Loop through each domain and check its status
for domain in domains:
    try:
        w = whois.whois(domain)
        if w.status == None:
            print(f"{domain} is available.")
        else:
            print(f"{domain} is registered.")
    except:
        print(f"{domain} could not be checked.")
