import socket
import time
import subprocess
from termcolor import colored


def clear_dns_cache():
    subprocess.call(["sudo", "killall", "-HUP", "mDNSResponder"])


domain_names = [
    "muchen.fan",
    "ai.muchen.fan",
    "mc.muchen.fan",
    "fmc.ai",
    "lawin.one",
]

for domain_name in domain_names:
    clear_dns_cache()

    print(domain_name, end="")

    try:
        start_time = time.time()
        ip_address = socket.gethostbyname(domain_name)
        end_time = time.time()

        resolving_time = end_time - start_time

        print(colored(" => " + ip_address, "light_blue"), end="")
        print(colored(
            " == {:.2f} s".format(resolving_time), "light_blue"))

    except:
        print(colored(" * Error: Unable to resolve hostname", "red"))
