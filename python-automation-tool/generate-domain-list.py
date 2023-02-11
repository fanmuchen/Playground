import itertools
import csv

# Generate all possible combinations of three letters
combinations = itertools.product("cfm", repeat=3)

# Create list of all .ai domains with three letters in second level
domains = []
for combination in combinations:
    domain = "".join(combination) + ".ai"
    domains.append(domain)

# Print list of domains
for domain in domains:
    print(domain)

# Create a .csv file and write the list of domains
with open('domains.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(domains)

print("Domains exported successfully to domains.csv")
